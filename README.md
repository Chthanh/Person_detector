# Person detector with simple web app 

## 📌 Introduction
This is a project that includes a **backend (FastAPI)** and **MongoDB** for processing user-uploaded images. The system:
- Allows users to **upload an image**.
- **Counts the number of people in the image** and **draws bounding boxes**.
- Returns the processed image along with the number of people in the image.
- **Stores image information in MongoDB** (filename, number of people, upload time).

<!-- ## 📂 Folder Structure
```
📦 project-folder
 ┣ 📂 backend
 ┃ ┣ 📂 ckpt
 ┃ ┃ ┗ yolo11n.pt
 ┃ ┣ 📜 database.py
 ┃ ┣ 📜 detection.py
 ┃ ┗ 📜 models.py
 ┣ 📂 frontend
 ┃ ┗ 📜 index.html
 ┣ 📜 docker-compose.yml
 ┗ 📜 README.md
``` -->

## 🛠 System Requirements
- **Docker** & **Docker Compose**
- **MongoDB Compass** (if you want to check the database)

## 🚀 How to Run the Project on Another Machine
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Chthanh/Person_detector.git
cd Person_detector
```

### 2️⃣ Chạy Docker Compose
```sh
docker-compose up --build
```
This command will:
- Create a backend (FastAPI) container running on port 8000.
- Create a MongoDB container to store image information.

### 3️⃣ Check if the API is Running
Open a browser and access:
```
http://localhost:8000/
```
<!-- 
### 4️⃣ Upload an Image via API
```sh
curl -X 'POST' 'http://localhost:8000/upload?num_people=3' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'file=@test.jpg'
```
📌 If successful:
```json
{
    "message": "File uploaded successfully",
    "file_id": "65f23a8d9a3b5a7c6c8e1234"
}
``` -->

### 5️⃣ Kiểm tra dữ liệu trong MongoDB
Nếu bạn muốn kiểm tra dữ liệu đã lưu vào MongoDB:
```sh
docker exec -it <mongo-container-id> mongosh
use image_db
db.uploads.find().pretty()
```

<!-- ## ❌ Xử lý lỗi
- **Không kết nối được MongoDB**: Kiểm tra container MongoDB đã chạy chưa bằng lệnh:
```sh
docker ps
```
- **Lỗi truy cập API**: Kiểm tra logs backend:
```sh
docker logs <backend-container-id>
``` -->

## 📌 Conclusion
This project helps you easily deploy an image processing system with FastAPI and MongoDB, which can be extended for various AI applications. 🚀


Let me know if you need any adjustments! 🚀
