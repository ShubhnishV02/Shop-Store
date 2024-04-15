from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from store.forms import CustomUserForm


def SIGNUP(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect("/login")
    context = {'form': form}
    return render(request, "auth/Signup.html", context)


def LOGIN(request):
    if request.user.is_authenticated:           #this if condition is used when user already logged in and try to login again.
        messages.warning(request, "You are already logged in")
        return redirect("home")
    else:
        if request.method == "POST":
            name = request.POST.get("username")
            pwd = request.POST.get("password")

            user = authenticate(request, username=name, password=pwd)

            if user is not None:
                login(request,user)
                messages.success(request, "Login Successfully")
                return redirect("home")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("/login")
        return render(request, "auth/Login.html")
    

def LOGOUT(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully")
    return redirect("home")