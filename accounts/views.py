from django.shortcuts import render, redirect

# Create your views here.
def signup_page(request):
    if request.method == "POST":
        return redirect("/accounts/me/")
    return render(request, "signup.html")


def account_page(request):
    return render(request, "account.html")
