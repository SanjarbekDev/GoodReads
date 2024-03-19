from django.test import TestCase
from users.models import CustomUser
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

        user = CustomUser.objects.get(username='sancho')
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

        user_count = CustomUser.objects.count()

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

        user_count = CustomUser.objects.count()

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

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response,'form','username','A user with that username already exists.')

class LoginUserTestCase(TestCase):

    def setUp(self):
        self.db_user = CustomUser.objects.create(username = "Sanjey", first_name = "Sanjarbek")
        self.db_user.set_password("somepass")
        self.db_user.save()

    def test_successfuly_login(self):

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

        self.client.post(
            reverse("users:login"),
            {
                'username' : 'Sanjey',
                'password' : 'pass'
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def logout_user(self):
        self.client.login(username='Sanjey', password='somepass')
        self.client.get(reverse("user:logout"))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

class ProfileTestCase(TestCase):
    def test_user_login_requared(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('users:login') + '?next=/users/profile/')

    def test_user_login_detials(self):
        user = CustomUser.objects.create(
                                    username = "Sanjey", 
                                    first_name = "Sanjarbek",
                                    email = 'tommy@gmail.com',
                        )
        user.set_password("passphrase")
        user.save()

        self.client.login(username='Sanjey', password='passphrase')
        ress = self.client.get(reverse('users:profile'))

        self.assertEquals(ress.status_code, 200)

        self.assertContains(ress, user.username)
        self.assertContains(ress, user.first_name)
        self.assertContains(ress, user.email)

    def test_profile_update(self):
        user = CustomUser.objects.create(
                                    username = "Sanjey", 
                                    first_name = "Sanjarbek",
                                    last_name = "Sodiqov",
                                    email = 'tommy@gmail.com',
                        )
        
        user.set_password("passwd")
        user.save()

        self.client.login(username='Sanjey', password='passwd')

        respons = self.client.post(
            reverse("users:profile_edit"),
            data={
                'username': 'test_user',
                'frist_name': 'Sanjarbek',
                'last_name' : 'Sodiqov',
                'email' : 'sanj1@gmail.com'
            }
        )

        # user = CustomUser.objects.get(pk=user.pk)

        user.refresh_from_db()

        self.assertEquals(user.username, 'test_user')
        self.assertEquals(user.email, 'sanj1@gmail.com')

        self.assertEqual(respons.url, reverse('users:profile'))
        