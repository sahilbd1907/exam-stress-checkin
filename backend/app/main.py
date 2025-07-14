from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.v1 import analyze

# Optional: loads .env manually
load_dotenv()

app = FastAPI()

app.include_router(analyze.router, prefix="/api/v1/analyze", tags=["Analyze"])

@app.get("/")
async def root():
    return {"message": "Exam Stress Check-In API running"}
