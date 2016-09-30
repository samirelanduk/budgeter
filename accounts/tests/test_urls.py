from budgeter.tests import UrlTest
from accounts import views

class HomeUrlTests(UrlTest):

    def test_signup_url_resolves_to_signup_view(self):
        self.check_url_returns_view("/accounts/signup/", views.signup_page)
