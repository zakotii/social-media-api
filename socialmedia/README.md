# Social Media API 📱🚀  

This project is a RESTful API for a social network, developed using **Django REST Framework**.  

## 📌 Features  

✅ User registration and authentication (JWT)  
✅ Profile creation and editing  
✅ Following and unfollowing users  
✅ Creating, viewing, and deleting posts  
✅ Likes and comments (optional)  
✅ Searching posts by hashtags  
✅ Scheduled posts with Celery (optional)  

## ⚙️ Installation and Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/ТВОЙ_ГИТХАБ/social-media-api.git
cd social-media-api

Creating a virtual environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

Installing dependencies
pip install -r requirements.txt

Using migrations
python manage.py migrate

Creating a superuser
python manage.py createsuperuser

 Starting the server
 python manage.py runserver


 Authentication (JWT)
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "admin", "password": "yourpassword"}'

Answer:
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}

Use access_token in the Authorization header:
-H "Authorization: Bearer your_access_token"


API Documentation
http://127.0.0.1:8000/schema/swagger-ui/


