from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .form import ChangeUserData, ProfileForm, UserForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import ProfileModel
from car.models import CarModel

class singupView(FormView):
    template_name = "form.html"
    form_class = UserForm
    success_url = reverse_lazy("loginpage")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'SingUp'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        return super().dispatch(request, *args, **kwargs)
    
class loginView(LoginView):
    template_name = 'form.html'

    def form_valid(self, form):
        messages.success(self.request, "Logged Successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy("profilepage")
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class logoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("loginpage")  

@login_required
def profile(request):
    profile, created = ProfileModel.objects.get_or_create(user=request.user)
    cars = profile.car.all()
    return render(request, "profile.html", {'car':cars})

def buyNow(request, id):
    car = get_object_or_404(CarModel, pk=id)
    car.quantity = car.quantity - 1
    car.save()
    profile, created = ProfileModel.objects.get_or_create(user=request.user)
    profile.car.add(car)
    return redirect("profilepage")


@login_required
def change_data(request):
    if request.method == 'POST':
        change_form = ChangeUserData(request.POST, instance = request.user)
        if change_form.is_valid():
            change_form.save()
            return redirect("profilepage")
    else:
        change_form = ChangeUserData(instance = request.user)
    return render(request, "form.html", {'form':change_form, 'type':'Data'})

@login_required
def change_pass_with(request):
    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, data = request.POST)
        if change_form.is_valid():
            change_form.save()
            return redirect("loginpage")
    else:
        change_form = PasswordChangeForm(user = request.user)
    return render(request, "form.html", {'form':change_form, 'type':'Password with old Password'})

@login_required
def profile_edit(request):
    return render(request, "edit.html")

