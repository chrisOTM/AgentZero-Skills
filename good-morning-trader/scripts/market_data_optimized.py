#!/usr/bin/env python3
"""
Good Morning Trader - Optimized Market Data Collector
Avoid web scraping, use reliable APIs and browser_agent calls
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
import json
import os

# Cache for data that doesn't change frequently (24h)
CACHE_FILE = "/tmp/gmt_cache.json"
CACHE_DURATION = 3600  # 1 hour

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                cache = json.load(f)
                # Check expiration
                if time.time() - cache.get('timestamp', 0) < CACHE_DURATION:
                    return cache.get('data', {})
        except:
            pass
    return {}

def save_cache(data):
    cache = {
        'timestamp': time.time(),
        'data': data
    }
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f)
    except:
        pass

def get_vix_data():
    """Get VIX and VIX term structure from yfinance"""
    try:
        # VIX spot
        vix = yf.Ticker("^VIX")
        vix_hist = vix.history(period="2d")
        vix_spot = vix_hist['Close'].iloc[-1]
        
        # VIX term structure - use available futures/ETNs
        # ^VIX3M, ^VIX6M symbols might not exist; using proxies
        vix_class = "Normal (<18) 🟢"
        if vix_spot < 18:
            vix_class = "Normal (<18) 🟢"
        elif vix_spot < 25:
            vix_class = "Elevated (18-25) 🟡"
        elif vix_spot < 35:
            vix_class = "Fear Zone (25-35) 🔴"
        else:
            vix_class = "Panic (>35) 🔴"
        
        # Get VVIX if available
        try:
            vvix = yf.Ticker("^VVIX")
            vvix_hist = vvix.history(period="2d")
            vvix_val = vvix_hist['Close'].iloc[-1]
        except:
            vvix_val = None
        
        return {
            'vix_spot': round(vix_spot, 2),
            'vix_class': vix_class,
            'prev_close': round(vix_hist['Close'].iloc[-2], 2) if len(vix_hist) > 1 else None,
            'vvix': round(vvix_val, 2) if vvix_val else None
        }
    except Exception as e:
        return {'error': f'VIX data error: {str(e)[:100]}'}

def get_spx_data():
    """Get SPX/SPY technical data via yfinance"""
    try:
        spy = yf.Ticker("SPY")
        spy_hist = spy.history(period="3mo")
        
        current = spy_hist['Close'].iloc[-1]
        prev_close = spy_hist['Close'].iloc[-2] if len(spy_hist) > 1 else current
        
        # Calculate SMAs
        sma_20 = spy_hist['Close'].rolling(20).mean().iloc[-1]
        sma_50 = spy_hist['Close'].rolling(50).mean().iloc[-1]
        sma_200 = spy_hist['Close'].rolling(200).mean().iloc[-1]
        
        # Percentage above moving averages
        above_20sma = (current - sma_20) / sma_20 * 100
        above_50sma = (current - sma_50) / sma_50 * 100
        above_200sma = (current - sma_200) / sma_200 * 100
        
        return {
            'spy_current': round(current, 2),
            'spy_change': round((current - prev_close) / prev_close * 100, 2),
            'sma_20': round(sma_20, 2),
            'sma_50': round(sma_50, 2),
            'sma_200': round(sma_200, 2),
            'above_20sma': round(above_20sma, 2),
            'above_50sma': round(above_50sma, 2),
            'above_200sma': round(above_200sma, 2)
        }
    except Exception as e:
        return {'error': f'SPX data error: {str(e)[:100]}'}

def get_global_markets():
    """Get global market data"""
    cache = load_cache()
    if 'global_markets' in cache:
        return cache['global_markets']
        
    try:
        # Major indices
        indices = {
            'nikkei': '^N225',
            'dax': '^GDAXI',
            'ftse': '^FTSE',
            'shanghai': '000001.SS'
        }
        
        result = {}
        for name, symbol in indices.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="2d")
                if len(hist) > 1:
                    current = hist['Close'].iloc[-1]
                    prev = hist['Close'].iloc[-2]
                    change = (current - prev) / prev * 100
                    result[name] = round(current, 2)
                    result[f'{name}_change'] = round(change, 2)
                elif len(hist) == 1:
                    result[name] = round(hist['Close'].iloc[-1], 2)
                    result[f'{name}_change'] = 0
            except:
                continue
        
        # Update cache
        cache_data = cache.copy()
        cache_data['global_markets'] = result
        save_cache(cache_data)
        
        return result
    except Exception as e:
        return {'error': f'Global markets error: {str(e)[:100]}'}

def get_macro_assets():
    """Get bonds, gold, oil"""
    cache = load_cache()
    if 'macro_assets' in cache:
        return cache['macro_assets']
    
    try:
        assets = {
            '10y_yield': '^TNX',
            'gold': 'GC=F',
            'oil': 'CL=F',
            'dollar_index': 'DX-Y.NYB'
        }
        
        result = {}
        for name, symbol in assets.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="2d")
                if len(hist) > 1:
                    current = hist['Close'].iloc[-1]
                    prev = hist['Close'].iloc[-2]
                    if name == '10y_yield':
                        change = current - prev  # basis points
                    else:
                        change = (current - prev) / prev * 100
                    result[name] = round(current, 2)
                    result[f'{name}_change'] = round(change, 2)
                elif len(hist) == 1:
                    result[name] = round(hist['Close'].iloc[-1], 2)
                    result[f'{name}_change'] = 0
            except:
                continue
        
        # Update cache
        cache_data = cache.copy()
        cache_data['macro_assets'] = result
        save_cache(cache_data)
        
        return result
    except Exception as e:
        return {'error': f'Macro assets error: {str(e)[:100]}'}

def get_market_breadth():
    """Get market breadth indicators (cached)"""
    cache = load_cache()
    if 'market_breadth' in cache:
        return cache['market_breadth']
    
    # Using browser_agent for this data would be optimal
    # For now, return placeholder with timestamp
    result = {
        'sp500_above_50ma': None,
        'sp500_above_200ma': None,
        'advance_decline': None,
        'timestamp': datetime.now().isoformat()
    }
    
    cache_data = cache.copy()
    cache_data['market_breadth'] = result
    save_cache(cache_data)
    
    return result

def generate_briefing():
    """Generate complete briefing with fallbacks"""
    print(f"\n=== GATHERING MARKET DATA ===\n")
    
    # Collect all data with timing
    start_time = time.time()
    
    print("1. VIX Data...")
    vix_data = get_vix_data()
    
    print("2. SPX Data...")
    spx_data = get_spx_data()
    
    print("3. Global Markets...")
    global_data = get_global_markets()
    
    print("4. Macro Assets...")
    macro_data = get_macro_assets()
    
    print("5. Market Breadth...")
    breadth_data = get_market_breadth()
    
    elapsed = time.time() - start_time
    print(f"\nData collection completed in {elapsed:.1f} seconds\n")
    
    # Buying power calculation based on VIX
    vix_spot = vix_data.get('vix_spot', 0)
    max_allocation = 25  # default
    if vix_spot < 15:
        max_allocation = 25
    elif vix_spot < 20:
        max_allocation = 30
    elif vix_spot < 30:
        max_allocation = 35
    elif vix_spot < 40:
        max_allocation = 40
    else:
        max_allocation = 50
    
    # Generate output
    print(f"""
# MARKET DATA BRIEFING - {datetime.now().strftime('%Y-%m-%d %H:%M')}

## VOLATILITY (yfinance)
- VIX Spot: {vix_data.get('vix_spot', 'N/A')} | {vix_data.get('vix_class', 'N/A')}
- VVIX: {vix_data.get('vvix', 'N/A')}
- Previous Close: {vix_data.get('prev_close', 'N/A')}
- Max Buying Power Allocation: {max_allocation}%

## SPX/SPY TECHNICAL
- SPY Current: ${spx_data.get('spy_current', 'N/A')} ({spx_data.get('spy_change', 'N/A')}%)
- 20-SMA: ${spx_data.get('sma_20', 'N/A')} | Above SMA: {spx_data.get('above_20sma', 'N/A')}%
- 50-SMA: ${spx_data.get('sma_50', 'N/A')} | Above SMA: {spx_data.get('above_50sma', 'N/A')}%
- 200-SMA: ${spx_data.get('sma_200', 'N/A')} | Above SMA: {spx_data.get('above_200sma', 'N/A')}%

## GLOBAL MARKETS
- Nikkei 225: {global_data.get('nikkei', 'N/A')} ({global_data.get('nikkei_change', 'N/A')}%)
- DAX: {global_data.get('dax', 'N/A')} ({global_data.get('dax_change', 'N/A')}%)
- FTSE 100: {global_data.get('ftse', 'N/A')} ({global_data.get('ftse_change', 'N/A')}%)

## MACRO ASSETS
- 10Y Treasury: {macro_data.get('10y_yield', 'N/A')}% ({macro_data.get('10y_yield_change', 'N/A')} bps)
- Gold: ${macro_data.get('gold', 'N/A')} ({macro_data.get('gold_change', 'N/A')}%)
- WTI Oil: ${macro_data.get('oil', 'N/A')} ({macro_data.get('oil_change', 'N/A')}%)
- US Dollar Index: {macro_data.get('dollar_index', 'N/A')} ({macro_data.get('dollar_index_change', 'N/A')}%)

## MARKET BREADTH (Cached)
- Last Updated: {breadth_data.get('timestamp', 'N/A')}

## DTE RECOMMENDATION (VIX {vix_spot})
- Min DTE: {'60+' if vix_spot > 25 else '45'}
- Target DTE: {'60-80' if vix_spot > 25 else '45-60'}
- Rationale: {'High VIX requires more time for mean reversion' if vix_spot > 25 else 'Moderate DTE for normal volatility'}

## PERFORMANCE
- Data retrieval time: {elapsed:.1f}s
- Cached elements: {len(load_cache())}

Note: For sentiment data (Fear & Greed, Put/Call, AAII) use browser_agent for reliable extraction.
""")

if __name__ == "__main__":
    generate_briefing()