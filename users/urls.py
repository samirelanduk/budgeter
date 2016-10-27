from django.conf.urls import url
from users import views

urlpatterns = [
    url(r"^signup/$", views.signup_page, name="signup_page"),
    url(r"^login/$", views.login_page, name="login_page"),
    url(r"^me/$", views.account_page, name="account_page")
]