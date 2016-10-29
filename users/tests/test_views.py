from django.contrib.auth.models import User
from budgeter.tests import ViewTest

class SignUpViewTests(ViewTest):

    def setUp(self):
        ViewTest.setUp(self)
        self.client.logout()


    def test_signup_view_uses_signup_template(self):
        response = self.client.get("/users/signup/")
        self.assertTemplateUsed(response, "signup.html")


    def test_signup_view_redirects_to_me_upon_POST(self):
        response = self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertRedirects(response, "/users/me/")


    def test_signup_view_can_create_account(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 3)
        user = User.objects.last()
        self.assertEqual(user.first_name, "Isaac")
        self.assertEqual(user.last_name, "Jones")
        self.assertEqual(user.email, "xyz@abc.xy")


    def test_signup_view_will_sign_in_new_user(self):
        self.assertNotIn("_auth_user_id", self.client.session)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertIn("_auth_user_id", self.client.session)


    def test_signup_view_will_not_use_existing_email(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "p1@s.com",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_signup_view_requires_first_names(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/signup/", data={
         "firstname": "",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_signup_view_requires_last_names(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_signup_view_requires_email(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_signup_view_requires_password(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": ""
        })
        self.assertEqual(User.objects.count(), 2)




class AccountViewTests(ViewTest):

    def test_account_view_uses_account_template(self):
        response = self.client.get("/users/me/")
        self.assertTemplateUsed(response, "account.html")


    def test_account_view_requires_user_be_logged_in(self):
        self.client.logout()
        response = self.client.get("/users/me/")
        self.assertRedirects(response, "/users/login/")



class LoginViewTests(ViewTest):

    def setUp(self):
        ViewTest.setUp(self)
        self.client.logout()


    def test_login_view_uses_login_template(self):
        response = self.client.get("/users/login/")
        self.assertTemplateUsed(response, "login.html")


    def test_login_view_redirects_to_home(self):
        response = self.client.post("/users/login/", data={
         "email": "p1@s.com",
         "password": "secret1"
        })
        self.assertRedirects(response, "/")


    def test_login_view_will_log_in_user(self):
        self.assertNotIn("_auth_user_id", self.client.session)
        self.client.post("/users/login/", data={
         "email": "p1@s.com",
         "password": "secret1"
        })
        self.assertIn("_auth_user_id", self.client.session)


    def test_login_view_wont_accept_wrong_details(self):
        self.assertNotIn("_auth_user_id", self.client.session)
        response = self.client.post("/users/login/", data={
         "email": "xxx@s.com",
         "password": "xxxxx"
        })
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertTrue(response.context["credentials_incorrect"])



class LogoutViewTests(ViewTest):

    def test_logout_view_can_actually_logout(self):
        self.client.logout()
        self.client.login(username="p1@s.com", password="secret1")
        self.assertIn("_auth_user_id", self.client.session)
        response = self.client.get("/users/logout/")
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertRedirects(response, "/")
