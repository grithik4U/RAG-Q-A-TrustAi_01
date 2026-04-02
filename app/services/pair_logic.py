PAIRS = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD", "AUDUSD", "NZDUSD", "USDCAD", "USDCHF"]


def pair_move(pair: str, currency: str, bias: str) -> str:
    pair = pair.upper()
    currency = currency.upper()
    bias = bias.lower()

    if bias == "neutral":
        return "neutral"

    if pair == "XAUUSD":
        if currency == "USD":
            return "down" if bias == "bullish" else "up"
        return "neutral"

    if len(pair) != 6:
        return "neutral"

    base, quote = pair[:3], pair[3:]

    if bias == "bullish":
        if base == currency:
            return "up"
        if quote == currency:
            return "down"
    elif bias == "bearish":
        if base == currency:
            return "down"
        if quote == currency:
            return "up"

    return "neutral"


def map_all_pairs(currency: str, bias: str) -> dict:
    return {pair: pair_move(pair, currency, bias) for pair in PAIRS}
