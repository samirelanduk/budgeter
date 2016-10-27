from budgeter.tests import UrlTest
from accounts import views

class HomeUrlTests(UrlTest):

    def test_signup_url_resolves_to_signup_view(self):
        self.check_url_returns_view("/accounts/signup/", views.signup_page)


    def test_me_url_resolves_to_me_view(self):
        self.check_url_returns_view("/accounts/me/", views.account_page)
