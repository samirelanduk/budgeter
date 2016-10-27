from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
        return redirect("/accounts/me/")
    return render(request, "signup.html")


def account_page(request):
    return render(request, "account.html")
