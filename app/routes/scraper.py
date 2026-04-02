from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup

router = APIRouter(prefix="/scraper", tags=["scraper"])

@router.get("/forex-factory")
def fetch_forex_factory():
    url = "https://www.forexfactory.com/calendar"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    events = []
    rows = soup.select("tr.calendar__row")

    for row in rows[:20]:
        try:
            currency = row.select_one(".calendar__currency").text.strip()
            event = row.select_one(".calendar__event").text.strip()
            impact = row.select_one(".calendar__impact span").get("title", "low")

            events.append({
                "currency": currency,
                "event": event,
                "impact": impact
            })
        except:
            continue

    return {"events": events}
