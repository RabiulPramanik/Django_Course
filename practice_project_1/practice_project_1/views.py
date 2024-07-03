from django.http import HttpResponse

def Student(request):
    return HttpResponse("This is Student page!")
def Teacher(request):
    return HttpResponse("This is Teacher page!")
def Home(request):
    return HttpResponse("This is Home page!")