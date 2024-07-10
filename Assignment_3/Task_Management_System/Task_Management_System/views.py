from django.shortcuts import render
from taskcategory.models import TaskCategory
from taskmodel.models import TaskModel

def home(request):
    tcd = TaskCategory.objects.all()
    tmd = TaskModel.objects.all()
    return render(request,  "home.html", {'mdata': tmd, 'cdata': tcd})