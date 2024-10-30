# backend/app/config.py
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "todo_db")

# Conexión a MongoDB
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
todos_collection = database.get_collection("todos")
