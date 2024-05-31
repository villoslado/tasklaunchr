from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsTestCase(TestCase):
    def setUp(self):
        self.signup_url = reverse("signup")
        self.login_url = reverse("login")
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            email="testuser@example.com",
        )

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

        # Test valid signup
        response = self.client.post(
            self.signup_url,
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password": "newpassword123",
                "password_confirmation": "newpassword123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

        # Test valid login
        response = self.client.post(
            self.login_url,
            {"username_or_email": "testuser", "password": "password123"},
        )
        self.assertEqual(response.status_code, 302)

        # Test invalid login
        response = self.client.post(
            self.login_url,
            {"username_or_email": "wronguser", "password": "wrongpassword"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid login credentials")

    def test_duplicate_email_signup(self):
        response = self.client.post(
            self.signup_url,
            {
                "username": "anotheruser",
                "email": "testuser@example.com",
                "password": "anotherpassword123",
                "password_confirmation": "anotherpassword123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email is already in use.")

    def test_password_mismatch_signup(self):
        response = self.client.post(
            self.signup_url,
            {
                "username": "mismatchuser",
                "email": "mismatchuser@example.com",
                "password": "password123",
                "password_confirmation": "differentpassword",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords do not match")


"""
To run the tests, use the command python manage.py test accounts.
"""
