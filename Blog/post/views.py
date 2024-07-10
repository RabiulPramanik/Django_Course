from django.shortcuts import render, redirect
from .form import PostForm

def add_post(request):
    if request.method == 'POST':
        Post_form = PostForm(request.POST)
        if Post_form.is_valid():
            Post_form.save()
            return redirect("add_post")
    else:
        Post_form = PostForm()
    return render(request, "add_post.html", {'form': Post_form})
