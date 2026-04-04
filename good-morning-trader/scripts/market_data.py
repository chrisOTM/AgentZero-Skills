#!/usr/bin/env python3
"""
Good Morning Trader - Market Data Collector
Uses yfinance for reliable real-time market data
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_vix_data():
    """Get VIX and related volatility data"""
    try:
        vix = yf.Ticker("^VIX")
        vix_hist = vix.history(period="5d")
        vix_spot = vix_hist['Close'].iloc[-1]
        
        # Classification
        if vix_spot < 18:
            vix_class = "Normal (<18) 🟢"
        elif vix_spot < 25:
            vix_class = "Elevated (18-25) 🟡"
        elif vix_spot < 35:
            vix_class = "Fear Zone (25-35) 🔴"
        else:
            vix_class = "Panic (>35) 🔴"
        
        return {
            'vix_spot': round(vix_spot, 2),
            'vix_class': vix_class,
            'prev_close': round(vix_hist['Close'].iloc[-2], 2) if len(vix_hist) > 1 else None
        }
    except Exception as e:
        return {'error': f'VIX data unavailable: {e}'}

def get_spx_data():
    """Get SPX/SPY technical data"""
    try:
        spy = yf.Ticker("SPY")
        spy_hist = spy.history(period="3mo")
        
        current = spy_hist['Close'].iloc[-1]
        
        # Calculate SMAs
        sma_20 = spy_hist['Close'].rolling(20).mean().iloc[-1]
        sma_50 = spy_hist['Close'].rolling(50).mean().iloc[-1]
        sma_200 = spy_hist['Close'].rolling(200).mean().iloc[-1]
        
        # Previous day
        prev_close = spy_hist['Close'].iloc[-2]
        
        return {
            'spy_current': round(current, 2),
            'spy_change': round((current - prev_close) / prev_close * 100, 2),
            'sma_20': round(sma_20, 2),
            'sma_50': round(sma_50, 2),
            'sma_200': round(sma_200, 2),
            'above_20sma': current > sma_20,
            'above_50sma': current > sma_50,
            'above_200sma': current > sma_200
        }
    except Exception as e:
        return {'error': f'SPX data unavailable: {e}'}

def get_global_markets():
    """Get overnight and global market data"""
    try:
        # Nikkei
        nikkei = yf.Ticker("^N225")
        nikkei_hist = nikkei.history(period="5d")
        nikkei_current = nikkei_hist['Close'].iloc[-1]
        nikkei_prev = nikkei_hist['Close'].iloc[-2]
        nikkei_change = (nikkei_current - nikkei_prev) / nikkei_prev * 100
        
        # DAX
        dax = yf.Ticker("^GDAXI")
        dax_hist = dax.history(period="5d")
        dax_current = dax_hist['Close'].iloc[-1]
        dax_prev = dax_hist['Close'].iloc[-2]
        dax_change = (dax_current - dax_prev) / dax_prev * 100
        
        return {
            'nikkei': round(nikkei_current, 2),
            'nikkei_change': round(nikkei_change, 2),
            'dax': round(dax_current, 2),
            'dax_change': round(dax_change, 2)
        }
    except Exception as e:
        return {'error': f'Global data unavailable: {e}'}

def get_macro_assets():
    """Get bonds, gold, oil data"""
    try:
        # 10Y Treasury
        tnx = yf.Ticker("^TNX")
        tnx_hist = tnx.history(period="5d")
        ten_year = tnx_hist['Close'].iloc[-1]
        ten_year_change = ten_year - tnx_hist['Close'].iloc[-2]
        
        # Gold
        gold = yf.Ticker("GC=F")
        gold_hist = gold.history(period="5d")
        gold_current = gold_hist['Close'].iloc[-1]
        gold_change = (gold_current - gold_hist['Close'].iloc[-2]) / gold_hist['Close'].iloc[-2] * 100
        
        # Oil (WTI)
        oil = yf.Ticker("CL=F")
        oil_hist = oil.history(period="5d")
        oil_current = oil_hist['Close'].iloc[-1]
        oil_change = (oil_current - oil_hist['Close'].iloc[-2]) / oil_hist['Close'].iloc[-2] * 100
        
        return {
            'ten_year_yield': round(ten_year, 2),
            'ten_year_change': round(ten_year_change, 2),
            'gold': round(gold_current, 2),
            'gold_change': round(gold_change, 2),
            'oil': round(oil_current, 2),
            'oil_change': round(oil_change, 2)
        }
    except Exception as e:
        return {'error': f'Macro data unavailable: {e}'}

def get_buying_power_allocation(vix):
    """Calculate max buying power based on VIX"""
    if vix < 15:
        return 25
    elif vix < 20:
        return 30
    elif vix < 30:
        return 35
    elif vix < 40:
        return 40
    else:
        return 50

def generate_briefing():
    """Generate complete morning briefing data"""
    vix_data = get_vix_data()
    spx_data = get_spx_data()
    global_data = get_global_markets()
    macro_data = get_macro_assets()
    
    vix_spot = vix_data.get('vix_spot', 0)
    max_allocation = get_buying_power_allocation(vix_spot)
    
    print(f"""
# MARKET DATA BRIEFING - {datetime.now().strftime('%Y-%m-%d %H:%M')}

## VOLATILITY (yfinance: ^VIX)
- VIX Spot: {vix_data.get('vix_spot', 'N/A')} | {vix_data.get('vix_class', 'N/A')}
- Previous Close: {vix_data.get('prev_close', 'N/A')}
- Max Buying Power Allocation: {max_allocation}%

## SPX/SPY TECHNICAL (yfinance: SPY)
- SPY Current: ${spx_data.get('spy_current', 'N/A')} ({spx_data.get('spy_change', 'N/A')}%)
- 20-SMA: ${spx_data.get('sma_20', 'N/A')} | Above: {spx_data.get('above_20sma', 'N/A')}
- 50-SMA: ${spx_data.get('sma_50', 'N/A')} | Above: {spx_data.get('above_50sma', 'N/A')}
- 200-SMA: ${spx_data.get('sma_200', 'N/A')} | Above: {spx_data.get('above_200sma', 'N/A')}

## GLOBAL MARKETS
- Nikkei 225: {global_data.get('nikkei', 'N/A')} ({global_data.get('nikkei_change', 'N/A')}%)
- DAX: {global_data.get('dax', 'N/A')} ({global_data.get('dax_change', 'N/A')}%)

## MACRO ASSETS
- 10Y Treasury: {macro_data.get('ten_year_yield', 'N/A')}% ({macro_data.get('ten_year_change', 'N/A')} bps)
- Gold: ${macro_data.get('gold', 'N/A')} ({macro_data.get('gold_change', 'N/A')}%)
- WTI Oil: ${macro_data.get('oil', 'N/A')} ({macro_data.get('oil_change', 'N/A')}%)

## DTE RECOMMENDATION (VIX {vix_spot})
- Min DTE: {'60+' if vix_spot > 25 else '45'}
- Target DTE: {'60-80' if vix_spot > 25 else '45-60'}
- Rationale: {'High VIX requires more time for mean reversion' if vix_spot > 25 else 'Moderate DTE for normal volatility'}
""")

if __name__ == "__main__":
    generate_briefing()
