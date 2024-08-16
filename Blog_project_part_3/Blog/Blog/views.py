from django.shortcuts import render
from post.models import PostModel
from category.models import CategoryModel

def home(request, category_slug = None):
    data = PostModel.objects.all()
    if category_slug is not None:
        cd = CategoryModel.objects.get(slug = category_slug)
        data = PostModel.objects.filter(category = cd)
    category = CategoryModel.objects.all()
    return render(request, "index.html", {'data':data, 'category':category})