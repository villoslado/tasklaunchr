from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from accounts.forms import SignUpForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    email=email,
                    password=password,
                )
                login(request, user)
                return redirect("todo_list_list")
            else:
                form.add_error("password", "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]

            # Try to authenticate with username first
            user = authenticate(
                request,
                username=username_or_email,
                password=password,
            )

            if user is None:
                try:
                    user = User.objects.get(email=username_or_email)
                    user = authenticate(
                        request, username=user.username, password=password
                    )
                except User.DoesNotExist:
                    user = None

            if user is not None:
                login(request, user)
                return redirect("todo_list_list")
            else:
                form.add_error(None, "Invalid login credentials")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")
