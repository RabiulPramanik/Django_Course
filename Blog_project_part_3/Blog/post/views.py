from django.shortcuts import render, redirect
from .form import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import PostModel, CommentModel
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

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


# class based views for create post
@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = PostModel
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy("profilepage")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
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

# class based views for edit post
@method_decorator(login_required, name="dispatch")
class PostEditView(UpdateView):
    model = PostModel
    form_class = PostForm
    template_name = 'post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profilepage")

@login_required
def delete_post(request, id):
    dd = PostModel.objects.get(pk=id)
    dd.delete()
    return redirect("profilepage")

# class based views for delete post
@method_decorator(login_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = PostModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profilepage")

class DetailPostView(DetailView):
    model = PostModel
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comment = post.comment.all()
        comment_form = CommentForm()
        context["comments"] = comment
        context['comments_form'] = comment_form
        return context
    
