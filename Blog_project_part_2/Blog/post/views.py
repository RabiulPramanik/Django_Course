from django.shortcuts import render, redirect
from .form import PostForm
from django.contrib.auth.decorators import login_required
from .models import PostModel

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect("postpage")
    else:
        post_form = PostForm()
    return render(request, "post.html", {'form':post_form})

@login_required
def edit_post(request, id):
    ed = PostModel.objects.get(pk=id)
    edit_form = PostForm(instance=ed)
    if request.method == 'POST':
        edit_form = PostForm(request.POST, instance=ed)
        if edit_form.is_valid():
            edit_form.instance.author = request.user
            edit_form.save()
            return redirect("profilepage")
    else:
        edit_form = PostForm(instance=ed)
    return render(request, "post.html", {'form':edit_form})

@login_required
def delete_post(request, id):
    dd = PostModel.objects.get(pk=id)
    dd.delete()
    return redirect("profilepage")
