from django.test import TestCase
from users.userDB import *

class UserTestCase(TestCase):
    def setUp(self):
        new_user(
            first_name='Guilherme',
            last_name='Rosada',
            email='gui_rosada@hotmail.com',
        )
    def test_creation(self):
        """Testa se usuário foi criado corretamente"""
        user = User.objects.get(email="gui_rosada@hotmail.com")
        self.assertEqual(user.first_name, 'Guilherme')