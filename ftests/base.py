from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
         username="p1@s.com",
         email="p1@s.com",
         password="secret1",
         first_name="Persona",
         last_name="Una"
        )
        self.user1 = User.objects.create_user(
         username="p2@s.com",
         email="p2@s.com",
         password="secret2",
         first_name="Personette",
         last_name="Duo"
        )
        self.browser = webdriver.Chrome()


    def tearDown(self):
        self.browser.quit()
