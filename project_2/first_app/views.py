from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("this is first app home !")
def index(request):
    return render(request, "first_app/home.html")
