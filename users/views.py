from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def index(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "註冊成功")
            return redirect("pages:root")
        else:
            return render(req, "users/register.html")


def register(req):
    return render(req, "users/register.html")


def sign_in(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)

            messages.success(req, "登入成功")
            return redirect("pages:root")
        else:
            messages.error(req, "登入失敗")
            return redirect("users:sign_in")

    return render(req, "users/login.html")


def sign_out(req):
    if req.method == "POST":
        logout(req)
        messages.success(req, "登出成功")
        return redirect("pages:root")
