from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r"^signup/$", views.signup_page, name="signup_page"),
    url(r"^me/$", views.account_page, name="account_page")
]