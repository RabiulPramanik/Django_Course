from django.shortcuts import render, redirect
from .form import TaskmodelFrom
from .models import TaskModel

def taskmodel(request):
    if request.method == 'POST':
        modelForm = TaskmodelFrom(request.POST)
        if modelForm.is_valid():
            modelForm.save()
            return redirect("taskmodelpage")
    else:
        modelForm = TaskmodelFrom()
    return render(request,  "taskmodel.html",{'form':modelForm})

def complete(request, id):
    cd = TaskModel.objects.get(pk=id)
    cd.is_complete = True
    cd.save()
    return redirect("homepage")

def edit(request, id):
    ed = TaskModel.objects.get(pk=id)
    modelForm = TaskmodelFrom(instance=ed)
    if request.method == 'POST':
        modelForm = TaskmodelFrom(request.POST, instance=ed)
        if modelForm.is_valid():
            modelForm.save()
            return redirect("homepage")
    return render(request,  "taskmodel.html",{'form':modelForm})

def delete(request, id):
    dd = TaskModel.objects.get(pk=id)
    dd.delete()
    return redirect("homepage")


