from budgeter.tests import ViewTest

class SignUpViewTests(ViewTest):

    def test_signup_view_uses_signup_template(self):
        response = self.client.get("/accounts/signup/")
        self.assertTemplateUsed(response, "signup.html")
