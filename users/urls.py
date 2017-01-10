from django.conf.urls import url
from users import views

urlpatterns = [
    url(r"^signup/$", views.signup_page, name="signup_page"),
    url(r"^login/$", views.login_page, name="login_page"),
    url(r"^logout/$", views.logout_page, name="logout_page"),
    url(r"^delete/$", views.delete_account_page, name="delete_account_page"),
    url(r"^me/$", views.account_page, name="account_page")
]
