from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import analyze, dashboard

app = FastAPI(
    title="Exam Stress AI Backend",
    version="1.0.0"
)

# CORS (for React connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(analyze.router, prefix="/api/v1/analyze", tags=["Analyze"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["Dashboard"])

@app.get("/")
async def root():
    return {"message": "Exam Stress Check-In Backend Running 🚀"}
