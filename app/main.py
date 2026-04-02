from fastapi import FastAPI
from app.routes import events, scraper

app = FastAPI(title="Forex News AI Engine")

app.include_router(events.router)
app.include_router(scraper.router)

@app.get("/health")
def health():
    return {"status": "running"}
