# Social Media API 📱🚀

Этот проект — RESTful API для социальной сети, разработанный на **Django REST Framework**.

## 📌 Функциональность

✅ Регистрация и аутентификация пользователей (JWT)  
✅ Создание и редактирование профиля  
✅ Подписки (Follow/Unfollow)  
✅ Создание, просмотр и удаление постов  
✅ Лайки и комментарии (опционально)  
✅ Поиск постов по хештегам  
✅ Запланированные публикации с Celery (опционально)  

## ⚙️ Установка и запуск

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/ТВОЙ_ГИТХАБ/social-media-api.git
cd social-media-api

Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

Установка зависимостей
pip install -r requirements.txt

Применение миграций
python manage.py migrate

Создание суперпользователя
python manage.py createsuperuser

 Запуск сервера
 python manage.py runserver


 Аутентификация (JWT)
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "admin", "password": "yourpassword"}'

Ответ:
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}

Используйте access_token в заголовке Authorization:
-H "Authorization: Bearer your_access_token"


Документация API
http://127.0.0.1:8000/swagger/

