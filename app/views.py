from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/getlit/")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="app/register.html", context={"register_form": form})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/getlit/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect("/")


def home(request):
    return render(request, template_name="app/home.html")


def after_login(request):
    return render(request, template_name="app/homeafterlogin.html")


def get_lit(request):
    return render(request, template_name="app/quest.html")


def goal(request):
    return render(request, template_name="app/goal.html")


def your_plan(request):
    return render(request, template_name="app/bodytype.html")
