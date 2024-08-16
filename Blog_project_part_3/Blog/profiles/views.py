from django.shortcuts import render, redirect
from register.form import ChangeUserData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from post.models import PostModel
from category.models import CategoryModel

@login_required
def add_profile(request, category_slug=None):
    data = PostModel.objects.filter(author = request.user)
    if category_slug is not None:
        cd = CategoryModel.objects.get(slug = category_slug)
        data = PostModel.objects.filter(author = request.user, category = cd)
    category = CategoryModel.objects.all()
    return render(request, "profile.html", {'user':request.user, 'data':data, 'category':category})

@login_required
def change_data(request):
    if request.method == 'POST':
        change_form = ChangeUserData(request.POST, instance = request.user)
        if change_form.is_valid():
            change_form.save()
            messages.success(request, "Change data successfully!")
            return redirect("profilepage")
    else:
        change_form = ChangeUserData(instance = request.user)
    return render(request, "change.html", {'form':change_form, 'type':'Data'})

@login_required
def change_pass_with(request):
    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, data = request.POST)
        if change_form.is_valid():
            change_form.save()
            messages.success(request, "Change password successfully!")
            return redirect("profilepage")
    else:
        change_form = PasswordChangeForm(user = request.user)
    return render(request, "change.html", {'form':change_form, 'type':'Password with old Password'})

# def add_profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             change_form = ChangeUserData(request.POST, instance = request.user)
#             if change_form.is_valid():
#                 change_form.save()
#                 messages.success(request, "Change data successfully!")
#                 return redirect("profilepage")
#         else:
#             change_form = ChangeUserData(instance = request.user)
#         return render(request, "profile.html", {'form':change_form})
#     else:
#         return redirect("loginpage")
