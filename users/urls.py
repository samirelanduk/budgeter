from django.conf.urls import url
from users import views

urlpatterns = [
    url(r"^login/$", views.login_page, name="login_page"),
    url(r"^logout/$", views.logout_page, name="logout_page"),
    url(r"^users/delete/$", views.delete_account_page, name="delete_account_page"),
    url(r"^profile/$", views.profile_page, name="profile_page"),
    url(r"^$", views.home_page, name="home_page")
]
