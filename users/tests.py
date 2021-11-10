from django.test import TestCase
from users.userDB import *

class UserTestCase(TestCase):
    def setUp(self):
        data = {"first_name" :"Guilherme", "last_name": "Rosada", "email": "testUnico1@hotmail.com", "password": "techweb123"}
        new_user(**data)
    def test_creation(self):
        """Testa se usuário foi criado corretamente"""
        user = User.objects.get(email="testUnico1@hotmail.com")
        self.assertEqual(user.first_name, 'Guilherme')