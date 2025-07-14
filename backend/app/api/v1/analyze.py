from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class JournalInput(BaseModel):
    text: str

@router.post("/")
async def analyze_journal(input: JournalInput):
    # Placeholder for emotion classification + LIME + GPT response
    return {
        "emotion": "stressed",
        "explanation": ["exam", "pressure", "overwhelmed"],
        "advice": "Take a short break, try some deep breathing."
    }
