from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
         username="person1",
         email="p1@s.com",
         password="secret1"
        )
        self.user1 = User.objects.create_user(
         username="person2",
         email="p2@s.com",
         password="secret2"
        )
        self.browser = webdriver.Chrome()


    def tearDown(self):
        self.browser.quit()
