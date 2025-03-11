from pymongo import MongoClient

MONGO_URI = "mongodb://mongodb:27017"
DB_NAME = "ai_app_docker"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
image_collection = db["images"]