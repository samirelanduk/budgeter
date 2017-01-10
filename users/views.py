from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_page(request):
    if request.method == "POST":
        form_data = {}
        error = False
        if not request.POST["firstname"]:
            form_data["firstname_error"] = "You need to supply a first name."
            error = True
        else:
            form_data["firstname"] = request.POST["firstname"]
        if not request.POST["lastname"]:
            form_data["lastname_error"] = "You need to supply a last name."
            error = True
        else:
            form_data["lastname"] = request.POST["lastname"]
        if not request.POST["email"]:
            form_data["email_error"] = "You need to supply an email."
            error = True
        elif User.objects.filter(username=request.POST["email"]).exists():
            form_data["email_error"] = "There is already a user account with that email."
            form_data["email"] = request.POST["email"]
            error = True
        else:
            form_data["email"] = request.POST["email"]
        if not request.POST["password"]:
            form_data["password_error"] = "You need to supply a password."
            error = True

        if error:
            return render(request, "signup.html", form_data)
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


@login_required(login_url="/users/login/", redirect_field_name=None)
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


def delete_account_page(request):
    if request.method == "POST":
        user = User.objects.get(email=request.user.email)
        logout(request)
        user.delete()
        return redirect("/")
    return render(request, "deleteaccount.html")
