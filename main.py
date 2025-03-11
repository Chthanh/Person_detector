from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import shutil
import os
import logging
import datetime
from backend.database import image_collection
from backend.detection import detect_people
from backend.models import ImageRecord, ImageUploadResponse

app = FastAPI()

UPLOAD_FOLDER = "storage/uploads/"
PROCESSED_FOLDER = "storage/processed/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

logging.basicConfig(filename='my_log.log', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

logging.info("====== Start app ======")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("frontend/index.html", "r") as file:
        return file.read()

@app.get("/image/{filename}")
async def get_processed_image(filename: str):
    file_path = os.path.join(PROCESSED_FOLDER, filename)
    
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    logging.info(f"Received {file.filename}")

    # Process image: Dectect people & draw bounding box
    people_count, processed_path = detect_people(file_path)

    # log data into MongoDB
    image_doc = {
        "original_path": file_path,
        "processed_path": processed_path,
        "people_count": people_count,
        "upload_time": datetime.datetime.utcnow()
    }
    
    image_validate = ImageRecord(**image_doc)
    
    result = image_collection.insert_one(image_validate.model_dump())
    
    logging.info(f"Dectected {people_count} people in image and insert log ==> databse - {result.inserted_id}")

    return JSONResponse({
        "message": "File processed successfully",
        "people_count": people_count,
        "processed_image_url": processed_path
    })
    