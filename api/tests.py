from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "TestPassword123",
        }
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, 201)

    def test_user_registration(self):
        data = {"username": "testuser", "password": "testpassword123"}
        response = self.client.post("/api/register/", data)  # <-- этот URL проверьте
        self.assertEqual(response.status_code, 201)
