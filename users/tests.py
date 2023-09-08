from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.urls import reverse
import logging
# Create your tests here.

class RegTestCase(TestCase):
    def test_user_accaunt_is_created(self):
        self.client.post(
                    reverse('users:register'),
                    data={
                        'username' : 'sancho',
                        'first_name' : 'Sanjarbek',
                        'last_name'  : 'Sodiqov',
                        'email' : 'sana@gmail.com',
                        'password' : 'somepasswd'
                    }
        )

        user = User.objects.get(username='sancho')
        self.assertEqual(user.first_name, 'Sanjarbek')
        self.assertEqual(user.last_name, 'Sodiqov')
        self.assertEqual(user.email, 'sana@gmail.com')
        self.assertNotEqual(user.password, 'somepasswd')

        self.assertTrue(user.check_password("somepasswd"), 'somepasswd')

    def test_required_fields(self):

        response = self.client.post(
            reverse('users:register'),
            data={
                'first_name' : 'Sanjar',
                'email' : 'Sanjar@gmail.com'

            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response,'form','username','This field is required.')
        self.assertFormError(response,'form','password','This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
                    reverse('users:register'),
                    data={
                        'username' : 'sancho',
                        'first_name' : 'Sanjarbek',
                        'last_name'  : 'Sodiqov',
                        'email' : 'sana',
                        'password' : 'somepasswd'
                    }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response,'form','email','Enter a valid email address.')
        

    def test_unique_user(self):
        self.test_user_accaunt_is_created()

        response = self.client.post(
                    reverse('users:register'),
                    data={
                        'username' : 'sancho',
                        'first_name' : 'Sanjarbek',
                        'last_name'  : 'Sodiqov',
                        'email' : 'sana@gmail.com',
                        'password' : 'somepasswd'
                    }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response,'form','username','A user with that username already exists.')

class LoginUserTestCase(TestCase):
    def test_successfuly_login(self):
        db_user = User.objects.create(username = "Sanjey", first_name = "Sanjarbek")
        db_user.set_password("somepass")
        db_user.save()

        self.client.post(
            reverse("users:login"),
            {
                'username' : 'Sanjey',
                'password' : 'somepass'
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)


    def test_wrong_credentials(self):
        db_user = User.objects.create(username = "Sanjey", first_name = "Sanjarbek")
        db_user.set_password("somepass")
        db_user.save()

        self.client.post(
            reverse("users:login"),
            {
                'username' : 'Sanjey',
                'password' : 'pass'
            }
        )

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)


