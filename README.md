# Forex News AI Intelligence App

A complete MVP application that interprets macroeconomic news events into:
- what the news means
- which currency is affected
- bullish / bearish / neutral bias
- which pairs are impacted
- expected directional moves

This version does **not** take trades. It is a decision-support app for news interpretation.

## Features
- FastAPI backend
- Streamlit frontend
- Rule-based macro interpretation engine
- Optional AI explanation layer
- SQLite database for event history
- Sample seeded economic events
- JSON API endpoints
- Pair direction mapping for FX and gold

## Supported pairs
- EURUSD
- GBPUSD
- USDJPY
- XAUUSD
- AUDUSD
- NZDUSD
- USDCAD
- USDCHF
- EURJPY
- GBPJPY

## Supported event types
- Non-Farm Payrolls
- CPI m/m
- Core CPI m/m
- Unemployment Rate
- GDP q/q
- Interest Rate Decision
- Retail Sales m/m
- PMI
- Central Bank Statement

## Quick start

### 1. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:
```bash
python -m venv .venv
.venv\\Scripts\\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run backend
```bash
uvicorn app.main:app --reload
```

Backend docs:
- http://127.0.0.1:8000/docs

### 4. Run frontend
In another terminal:
```bash
streamlit run frontend/streamlit_app.py
```

## Environment variables
Create a `.env` file if you want AI explanations:
```env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini
```

The app works without AI. In that case it uses deterministic explanations.

## API endpoints

### Health
- `GET /health`

### Events
- `GET /events`
- `POST /events`
- `POST /events/interpret`
- `GET /events/{event_id}`

### Demo
- `POST /seed`

## Example payload
```json
{
  "event_name": "CPI m/m",
  "currency": "USD",
  "impact": "high",
  "actual": 0.4,
  "forecast": 0.2,
  "previous": 0.3
}
```

## Output example
```json
{
  "event_name": "CPI m/m",
  "currency": "USD",
  "currency_bias": "bullish",
  "strength": "strong",
  "interpretation": "Inflation came in higher than expected, which can support tighter monetary policy expectations and strengthen USD.",
  "affected_pairs": ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD"],
  "expected_moves": {
    "EURUSD": "down",
    "GBPUSD": "down",
    "USDJPY": "up",
    "XAUUSD": "down"
  },
  "confidence": 0.95
}
```

## Project structure
```text
RAG-Q-A-TrustAi_01/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed.py
│   ├── routes/
│   │   └── events.py
│   └── services/
│       ├── ai_explainer.py
│       ├── macro_engine.py
│       └── pair_mapper.py
├── frontend/
│   └── streamlit_app.py
├── requirements.txt
└── README.md
```
