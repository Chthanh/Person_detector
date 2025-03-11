from pydantic import BaseModel
from datetime import datetime

# Schema cho request upload ảnh
class ImageUploadResponse(BaseModel):
    message: str
    people_count: int
    processed_image_url: str

# Schema lưu dữ liệu vào MongoDB
class ImageRecord(BaseModel):
    original_path: str
    processed_path: str
    people_count: int
    upload_time: datetime