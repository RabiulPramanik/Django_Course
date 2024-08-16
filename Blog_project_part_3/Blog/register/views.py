from django.shortcuts import render, redirect
from .form import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

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
    
# class based views for login
class login_user_view(LoginView):
    template_name = 'register.html'
    def form_valid(self, form):
        messages.success(self.request, "Logged Successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, "Not valid information!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context
    
    def get_success_url(self):
        return reverse_lazy("profilepage")
    # success_url = reverse_lazy("profilepage")



def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("loginpage")
    else:
        return redirect("loginpage")
    
class logout_user_view(LogoutView):
    def get_success_url(self):
        return reverse_lazy("profilepage")
