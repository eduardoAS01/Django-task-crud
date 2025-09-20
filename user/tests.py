from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class UserTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = 'testuser',password='Qwerty1234.')
        self.url = reverse("task/list/")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,302)
        self.assertTrue(response.url.startswith("/user/sign_in/"))
        self.assertIn("next=",response.url)