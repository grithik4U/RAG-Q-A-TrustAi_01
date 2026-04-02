import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Next Level Forex AI Dashboard")

if st.button("Load Live News"):
    news = requests.get(f"{API}/scraper/forex-factory").json()
    st.write(news)

st.subheader("Auto Analysis")

if st.button("Analyze All High Impact"):
    data = requests.get(f"{API}/scraper/forex-factory").json()
    events = data.get("events", [])

    for e in events:
        if "High" in e.get("impact", ""):
            payload = {
                "event": e.get("event"),
                "currency": e.get("currency"),
                "actual": 0,
                "forecast": 0
            }
            result = requests.post(f"{API}/events/interpret-ai", json=payload).json()
            st.write(result)
