from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

MONGO_URI = config("MONGO_URI")  # Correct key matching .env
client = AsyncIOMotorClient(MONGO_URI)
db = client["exam_stress_db"]
journal_collection = db["journal_entries"]
