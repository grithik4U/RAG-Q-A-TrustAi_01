from fastapi import APIRouter
from app.services.ai_macro_engine import interpret_with_ai

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/interpret-ai")
def interpret(payload: dict):
    return interpret_with_ai(payload)
