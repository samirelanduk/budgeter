from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup_page(request):
    if request.method == "POST":
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
    return render(request, "login.html")
