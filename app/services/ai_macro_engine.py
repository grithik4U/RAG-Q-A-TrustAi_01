import os

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# fallback intelligent logic
def fallback_logic(payload):
    actual = payload.get("actual")
    forecast = payload.get("forecast")
    currency = payload.get("currency", "USD")

    if actual is None or forecast is None:
        bias = "neutral"
    elif actual > forecast:
        bias = "bullish"
    elif actual < forecast:
        bias = "bearish"
    else:
        bias = "neutral"

    return {
        "currency": currency,
        "bias": bias,
        "reason": "Fallback logic used"
    }


def interpret_with_ai(payload):
    if not OPENAI_KEY:
        result = fallback_logic(payload)
    else:
        # placeholder for real LLM call
        result = fallback_logic(payload)

    pairs = ["EURUSD","GBPUSD","USDJPY","XAUUSD"]

    moves = {}
    for pair in pairs:
        if result["bias"] == "bullish":
            moves[pair] = "depends"
        elif result["bias"] == "bearish":
            moves[pair] = "depends"
        else:
            moves[pair] = "neutral"

    return {
        "event": payload.get("event"),
        "currency": result["currency"],
        "bias": result["bias"],
        "expected_moves": moves,
        "reason": result["reason"]
    }
