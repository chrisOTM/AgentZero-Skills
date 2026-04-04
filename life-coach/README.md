# Life Coach

This skill provides structured coaching support for personal development, goal setting, habit building, motivation, decision-making, and self-reflection.
It is primarily written in German and is designed for conversational coaching workflows.

## Overview

`life-coach` is a guidance-oriented skill for users who want help with topics such as:

- personal development
- life planning
- goal setting
- building habits
- motivation and follow-through
- work-life balance
- career orientation
- relationships and communication
- self-reflection

## Main Files

- `life-coach/SKILL.md`

The skill definition includes:

- YAML frontmatter with metadata and trigger phrases
- a phased coaching process
- coaching interventions for common situations
- sample conversation patterns
- boundaries describing what coaching should not replace

## Typical Activation

This skill is intended to activate for prompts such as:

- `life coach`
- `coaching`
- `persönliche entwicklung`
- `zielsetzung`
- `motivation`
- `selbstreflexion`
- `ich bin unsicher`

See `SKILL.md` for the full trigger list.

## Workflow

The skill follows a practical coaching flow:

1. Clarify the current situation.
2. Identify values and priorities.
3. Define a vision and concrete goals.
4. Translate goals into actionable habits or plans.
5. Track progress with reviews and accountability.

It also includes response patterns for uncertainty, low motivation, overwhelm, and inner conflict.

## Intended Use

This skill works best for users who want reflective, structured coaching rather than one-off advice.
It is especially suited to clarifying priorities, building routines, and turning vague intentions into concrete next steps.

## Boundaries

This skill is for coaching support, not for professional medical, legal, financial, or psychotherapeutic care.
If the situation suggests a need for clinical or crisis support, the skill should direct the user toward appropriate professional help.

## Repository Notes

This repository does not currently define a formal build or test runner for skill files.
For changes to this skill, the main verification step is a careful review of:

- frontmatter structure
- heading order
- Markdown formatting
- consistency of terminology and language
- trigger phrases still matching the skill intent

See the repository-level `AGENTS.md` for broader agent guidance.
