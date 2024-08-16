from django.shortcuts import render, redirect
from .form import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def singup_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            register_form = RegistrationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Account Created Successfully")
                return redirect("singuppage")
        else:
            register_form = RegistrationForm()
        return render(request, "register.html", {'form': register_form, 'type':'Registration'})
    else:
        return redirect("profilepage")

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                user_pass = login_form.cleaned_data['password']
                user = authenticate(username=username, password=user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged Successfully")
                    return redirect("profilepage")
                else:
                    messages.warning(request, "Not valid information!")
                    return redirect('singuppage')
        else:
            login_form = AuthenticationForm()
        return render(request, "register.html", {'form': login_form, 'type':'Login'})
    else:
        return redirect("profilepage")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("loginpage")
    else:
        return redirect("loginpage")
