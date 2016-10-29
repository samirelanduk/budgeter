from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase

class BudgetTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
         username="p1@s.com",
         email="p1@s.com",
         password="secret1",
         first_name="Brad",
         last_name="Jones"
        )
        self.user1 = User.objects.create_user(
         username="p2@s.com",
         email="p2@s.com",
         password="secret2",
         first_name="Sheila",
         last_name="Belle"
        )
        self.client.login(username="p1@s.com", password="secret1")



class UrlTest(BudgetTest):

    def check_url_returns_view(self, url, view):
        resolver = resolve(url)
        self.assertEqual(resolver.func, view)



class ViewTest(BudgetTest):
    pass
