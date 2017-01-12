from django.contrib.auth.models import User
from budgeter.tests import ViewTest

class HomePageViewTests(ViewTest):

    def setUp(self):
        ViewTest.setUp(self)
        self.client.logout()


    def test_home_view_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


    def test_home_view_redirects_to_profile_upon_POST(self):
        response = self.client.post("/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertRedirects(response, "/profile/")


    def test_home_view_can_create_account(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/", data={
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


    def test_home_view_will_sign_in_new_user(self):
        self.assertNotIn("_auth_user_id", self.client.session)
        self.client.post("/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertIn("_auth_user_id", self.client.session)


    def test_home_view_will_not_use_existing_email(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "p1@s.com",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_home_view_requires_first_names(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/", data={
         "firstname": "",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_home_view_requires_last_names(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/", data={
         "firstname": "Isaac",
         "lastname": "",
         "email": "xyz@abc.xy",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_home_view_requires_email(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "",
         "password": "swordfish"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_home_view_requires_password(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/", data={
         "firstname": "Isaac",
         "lastname": "Jones",
         "email": "xyz@abc.xy",
         "password": ""
        })
        self.assertEqual(User.objects.count(), 2)



class ProfileViewTests(ViewTest):

    def test_profile_view_uses_profile_template(self):
        response = self.client.get("/profile/")
        self.assertTemplateUsed(response, "profile.html")


    def test_profile_view_requires_user_be_logged_in(self):
        self.client.logout()
        response = self.client.get("/profile/")
        self.assertRedirects(response, "/login/")



class LoginViewTests(ViewTest):

    def setUp(self):
        ViewTest.setUp(self)
        self.client.logout()


    def test_login_view_uses_login_template(self):
        response = self.client.get("/login/")
        self.assertTemplateUsed(response, "login.html")


    def test_login_view_redirects_to_home(self):
        response = self.client.post("/login/", data={
         "email": "p1@s.com",
         "password": "secret1"
        })
        self.assertRedirects(response, "/")


    def test_login_view_will_log_in_user(self):
        self.assertNotIn("_auth_user_id", self.client.session)
        self.client.post("/login/", data={
         "email": "p1@s.com",
         "password": "secret1"
        })
        self.assertIn("_auth_user_id", self.client.session)


    def test_login_view_wont_accept_wrong_details(self):
        self.assertNotIn("_auth_user_id", self.client.session)
        response = self.client.post("/login/", data={
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
        response = self.client.get("/logout/")
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertRedirects(response, "/")



class AccountDeletionViewTests(ViewTest):

    def test_account_deletion_view_uses_account_deletion_template(self):
        response = self.client.get("/users/delete/")
        self.assertTemplateUsed(response, "deleteaccount.html")


    def test_delete_account_view_requires_user_be_logged_in(self):
        self.client.logout()
        response = self.client.get("/users/delete/")
        self.assertRedirects(response, "/login/")


    def test_delete_view_redirects_to_home_upon_POST(self):
        response = self.client.post("/users/delete/", data={
         "password": "secret1"
        })
        self.assertRedirects(response, "/")


    def test_delete_view_wont_delete_with_wrong_password(self):
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post("/users/delete/", data={
         "password": "wrong"
        })
        self.assertEqual(User.objects.count(), 2)


    def test_delete_view_logs_user_out_on_POST(self):
        self.client.logout()
        self.client.login(username="p1@s.com", password="secret1")
        self.assertIn("_auth_user_id", self.client.session)
        response = self.client.post("/users/delete/", data={
         "password": "secret1"
        })
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertRedirects(response, "/")


    def test_delete_view_can_delete_users(self):
        self.assertEqual(User.objects.count(), 2)
        self.client.post("/users/delete/", data={
         "password": "secret1"
        })
        self.assertEqual(User.objects.count(), 1)
        remaining_user = User.objects.first()
        self.assertNotEqual(remaining_user.email, "p1@s.com")
