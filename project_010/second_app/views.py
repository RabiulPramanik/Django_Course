from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This  is courses page !")
def about(request):
    return HttpResponse("This is About page !")
def home(request):
    return HttpResponse("This is second app home !")
