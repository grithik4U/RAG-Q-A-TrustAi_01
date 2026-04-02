import os
from app.services.pair_logic import map_all_pairs

API_KEY = os.getenv("OPENAI_API_KEY")


def build_prompt(payload: dict) -> str:
    return f"""
You are a professional macro trading analyst.

Event: {payload.get('event')}
Currency: {payload.get('currency')}
Actual: {payload.get('actual')}
Forecast: {payload.get('forecast')}

Tasks:
1. Determine if this is bullish, bearish or neutral for the currency.
2. Give a short reasoning.
3. Provide strength (weak/moderate/strong).

Return JSON only:
{{
  "bias": "bullish/bearish/neutral",
  "strength": "weak/moderate/strong",
  "reason": "..."
}}
"""


def call_openai(prompt: str):
    # placeholder: safe fallback without external dependency
    return {
        "bias": "neutral",
        "strength": "weak",
        "reason": "LLM not connected yet"
    }


def interpret(payload: dict):
    prompt = build_prompt(payload)

    if API_KEY:
        ai_result = call_openai(prompt)
    else:
        ai_result = call_openai(prompt)

    moves = map_all_pairs(payload.get("currency", "USD"), ai_result["bias"])

    return {
        "event": payload.get("event"),
        "currency": payload.get("currency"),
        "bias": ai_result["bias"],
        "strength": ai_result["strength"],
        "reason": ai_result["reason"],
        "expected_moves": moves
    }
