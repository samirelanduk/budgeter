from budgeter.tests import ViewTest

class SignUpViewTests(ViewTest):

    def test_signup_view_uses_signup_template(self):
        response = self.client.get("/accounts/signup/")
        self.assertTemplateUsed(response, "signup.html")


    def test_signup_view_redirects_to_me_upon_POST(self):
        response = self.client.post("/accounts/signup/")
        self.assertRedirects(response, "/accounts/me/")



class AccountViewTests(ViewTest):

    def test_account_view_uses_account_template(self):
        response = self.client.get("/accounts/me/")
        self.assertTemplateUsed(response, "account.html")
