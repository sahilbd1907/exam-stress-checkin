from pydantic import BaseModel
from datetime import datetime

class JournalLog(BaseModel):
    text: str
    cleaned_text: str
    emotion: str
    explanation: list
    advice: str
    timestamp: datetime
