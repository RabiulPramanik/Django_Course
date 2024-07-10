from django.shortcuts import render, redirect
from .form import TaskcategoryFrom

def taskcategory(request):
    if request.method == 'POST':
        catagoryForm = TaskcategoryFrom(request.POST)
        if catagoryForm.is_valid():
            catagoryForm.save()
            return redirect("taskcategorypage")
    else:
        catagoryForm = TaskcategoryFrom()
    return render(request,  "taskcategory.html",{'form':catagoryForm})
