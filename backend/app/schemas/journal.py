from pydantic import BaseModel

class JournalInput(BaseModel):
    text: str
