from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_dashboard():
    return {
        "weekly_emotions": {"happy": 2, "stressed": 4, "calm": 1},
        "streak": 3
    }
