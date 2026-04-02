import streamlit as st
import requests

st.title("Forex AI News Dashboard")

api = "http://127.0.0.1:8000"

if st.button("Fetch Forex Factory News"):
    data = requests.get(f"{api}/scraper/forex-factory").json()
    st.write(data)

st.subheader("AI Interpretation")

actual = st.number_input("Actual", value=0.0)
forecast = st.number_input("Forecast", value=0.0)

if st.button("Interpret"):
    payload = {
        "event": "custom",
        "currency": "USD",
        "actual": actual,
        "forecast": forecast
    }
    result = requests.post(f"{api}/events/interpret-ai", json=payload).json()
    st.write(result)
