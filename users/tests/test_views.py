from django.contrib.auth.models import User
from budgeter.tests import ViewTest

class SignUpViewTests(ViewTest):

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
        self.assertEqual(User.objects.count(), 0)
        self.client.post("/users/signup/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
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




class AccountViewTests(ViewTest):

    def test_account_view_uses_account_template(self):
        response = self.client.get("/users/me/")
        self.assertTemplateUsed(response, "account.html")



class LoginViewTests(ViewTest):

    def test_login_view_uses_login_template(self):
        response = self.client.get("/users/login/")
        self.assertTemplateUsed(response, "login.html")


    def test_login_view_redirects_to_home(self):
        response = self.client.post("/users/login/", data={
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertRedirects(response, "/")