from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home page! HOME")

def contact(request):
    # pass
    return HttpResponse("This is contact page!")
def SendMe(request):
    return HttpResponse("this is SendMe page!")