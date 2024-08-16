from django.shortcuts import render

def add_category(request):
    return render(request, "category.html")
