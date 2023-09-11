from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect

from .models import *


# Create your views here.

def reg_page(request):
    if request.method == "GET":
        return render(request, "mainapp/reg_page.html")
    else:
        data = request.POST
        username = data["username"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password1, password2 = data["password1"], data["password2"]
        if username is None or first_name is None or last_name is None or email is None or password1 is None or password2 is None:
            return HttpResponse("<h3>Заполните все поля</h3>")
        elif password1 != password2:
            return HttpResponse("<h3>Пароли должны совпадать</h3>")
        else:
            newuser = User()
            newuser.create_user(username, first_name, last_name, email, password1)
            return redirect("../login/")


def log_page(request):
    if request.method == "GET":
        return render(request, "mainapp/log_page.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return HttpResponse("lg " + data["username"] + " пароль " + data["password"])
            login(request, user)
            return redirect("../note/")
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")


def logout_page(request):
    logout(request)
    return redirect("../login/")


def note(request):

    if request.user.is_authenticated:
        current_user = request.user
        notes = Note.objects.filter(user_id_id=current_user.id)
        context = {"notes": reversed(notes)}
        return render(request, "mainapp/note.html", context)
    else:
        return redirect("../login/")

def add(request):
    if request.method == "GET":
        return render(request, "mainapp/add.html")
    else:
        if request.user.is_authenticated:
            current_user = request.user
            data = request.POST
            nt = Note()
            nt.add(data["content"], current_user.id)
            return redirect("./")
        else:
            return redirect("../../login/")