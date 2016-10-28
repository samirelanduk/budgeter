from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_page(request):
    if request.method == "POST":
        if not request.POST["firstname"]:
            return render(request, "signup.html", {
             "firstname_error": "You need to supply a first name."
            })
        elif not request.POST["lastname"]:
            return render(request, "signup.html", {
             "lastname_error": "You need to supply a last name."
            })
        elif not request.POST["email"]:
            return render(request, "signup.html", {
             "email_error": "You need to supply an email."
            })
        elif User.objects.filter(username=request.POST["email"]).exists():
            return render(request, "signup.html", {
             "email_error": "There is already a user account with that email."
            })
        elif not request.POST["password"]:
            return render(request, "signup.html", {
             "password_error": "You need to supply a password."
            })
        else:
            User.objects.create_user(
             first_name=request.POST["firstname"],
             last_name=request.POST["lastname"],
             email=request.POST["email"],
             password=request.POST["password"],
             username=request.POST["email"]
            )
            user = authenticate(
             username=request.POST["email"],
             password=request.POST["password"]
            )
            login(request, user)
            return redirect("/users/me/")
    return render(request, "signup.html")


def account_page(request):
    return render(request, "account.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(
         username=request.POST["email"],
         password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"credentials_incorrect": True})
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/")
