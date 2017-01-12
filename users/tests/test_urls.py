from budgeter.tests import UrlTest
from users import views

class UsersUrlTests(UrlTest):

    def test_home_page_url_resolves_to_home_page_view(self):
        self.check_url_returns_view("/", views.home_page)


    def test_profile_url_resolves_to_profile_view(self):
        self.check_url_returns_view("/profile/", views.profile_page)


    def test_login_url_resolves_to_login_view(self):
        self.check_url_returns_view("/login/", views.login_page)


    def test_logout_url_resolves_to_logout_view(self):
        self.check_url_returns_view("/logout/", views.logout_page)


    def test_delete_url_resolves_to_delete_view(self):
        self.check_url_returns_view("/users/delete/", views.delete_account_page)
