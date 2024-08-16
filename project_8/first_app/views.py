from django.shortcuts import render, redirect
from .form import RegisterForm, DataChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def home(request):
    return render(request, "home.html")
def singup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfull')
                messages.warning(request, 'Warning')
                messages.info(request, 'info')
                form.save()
                print(form.cleaned_data)
                return redirect("singuppage")
        else:
            form = RegisterForm()
        return render(request, "./singup.html", {'form':form})
    else:
        return redirect('profilepage')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                # name = request.POST.get('username')
                # userpass = request.POST.get('password')
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request,user)
                    return redirect("profilepage")
        else:
            form = AuthenticationForm()
        return render(request, "./login.html", {'form':form})
    else:
        return redirect('profilepage')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, "./profile.html", {'user': request.user})
    else:
        return redirect("loginpage")

def user_logout(request):
    logout(request)
    return redirect("loginpage")

def pass_Change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profilepage")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "./passchange.html", {'form':form})
def pass_Change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profilepage")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "./passchange.html", {'form':form})

def datachange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DataChangeForm(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account Update Successfull')
                form.save()
                return redirect("datachangepage")
        else:
            form = DataChangeForm(instance = request.user)
        return render(request, "./datachange.html", {"form":form})
    else:
        return redirect("loginpage")

