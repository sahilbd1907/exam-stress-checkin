from fastapi import APIRouter
from app.db.connection import journal_collection

router = APIRouter()

@router.get("/")
async def test_mongo_connection():
    count = await journal_collection.count_documents({})
    return {"message": "Mongo connected", "document_count": count}
