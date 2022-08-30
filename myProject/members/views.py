from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    """
    A simple login with Django Auth
    status = 0 : Success Sign In
    status = 1 : Not Authenticate
    status = 2 : Need to sign in
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        """ Authenticate user """
        user = authenticate(request, username=username, password=password)
        """ If user us true login """
        if user is not None:
            login(request, user)
            return redirect("/members/sign_in/?status=0")
        else:
            return redirect("/members/sign_in/?status=1")

    """ Raise status if have some error in sign in POST """
    if request.method == "GET":
        status = request.GET.get("status")
        template = "registration/sign_in.html"
        context = {
            "status": status,
        }
        return render(request, template, context)


def sign_up(request):
    """
    A simple registration with Django Auth
    status = 0 : Success Sign Up
    status = 1 : Username or Email already exist
    status = 2 : Username empty
    status = 3 : Email empty
    status = 4 : Password empty
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        """ Check for empty username and password """
        if not username.strip():
            return redirect("/members/sign_up/?status=2")
        if not email.strip():
            return redirect("/members/sign_up/?status=3")
        if not password:
            return redirect("/members/sign_up/?status=4")

        """ Check if user and email already exist """
        user = User.objects.filter(username=username)
        mail = User.objects.filter(email=email)
        if user or mail:
            return redirect("/members/sign_up/?status=1")

        """ Create user """
        if username and password:
            new_user = User.objects.create_user(
                username=username, password=password, email=email
            )
            new_user.save()
            return redirect("/members/sign_up/?status=0")

    """ Raise status if have some error in sign up POST """
    if request.method == "GET":
        status = request.GET.get("status")
        template = "registration/sign_up.html"
        context = {
            "status": status,
        }
        return render(request, template, context)


def sign_out(request):
    """
    A simple logout with Django Auth
    """
    template = "main/index.html"
    context = {}

    if request.user.is_authenticated:
        logout(request)
        return render(request, template, context)
    else:
        return redirect("main:index")
