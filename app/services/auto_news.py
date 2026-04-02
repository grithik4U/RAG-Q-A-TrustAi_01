import time
import requests

FOREX_FACTORY_URL = "http://127.0.0.1:8000/scraper/forex-factory"


def fetch_news():
    try:
        res = requests.get(FOREX_FACTORY_URL)
        return res.json().get("events", [])
    except:
        return []


def filter_high_impact(events):
    return [e for e in events if "High" in e.get("impact", "")]


def auto_fetch_loop(interval=60):
    while True:
        events = fetch_news()
        high = filter_high_impact(events)
        print(f"Fetched {len(high)} high impact events")
        time.sleep(interval)
