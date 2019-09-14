from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_password_successful(self):
        """Test creating a new user with an email and password"""
        email = 'eliezer@test.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        """Test whether email gets normalized when a new user is created"""
        email = 'eliezer@GMail.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email.lower())

    def test_email_not_empty(self):
        """Test if email is empty or None"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user('', 'testPass')

    def test_create_super_user(self):
        """Test if superuser is created successfully or not"""
        user = get_user_model().objects.create_superuser('test_email@one.com', 'testpassword')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
