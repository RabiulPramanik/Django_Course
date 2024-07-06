from django.shortcuts import render
from . import form

def home(request):
    return render(request, "home.html")
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, "about.html", {'name':name,'email':email, 'select':select})
    else:
        return render(request, "about.html")
def from_input(request):
    return render(request, "form.html")

def django_form(request):
    if request.method=='POST':
        contactform = form.ContactForm(request.POST, request.FILES)
        if contactform.is_valid():
            file = contactform.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(contactform.cleaned_data)
            return render(request, "django_form.html", {'form': contactform})
    else:
        contactform = form.ContactForm()
    return render(request, "django_form.html", {'form': contactform})

def student_form(request):
    if request.method == 'POST':
        studentForm = form.StudentForm(request.POST)
        if studentForm.is_valid():
            print(studentForm.cleaned_data)
            return render(request, "student_form.html", {'form':studentForm})
    else:
        studentForm = form.StudentForm()
    return render(request, "student_form.html", {'form':studentForm})

def passward_valid(request):
    if request.method == 'POST':
        passwardForm = form.passward_valid(request.POST)
        if passwardForm.is_valid():
            print(passwardForm.cleaned_data)
            return render(request, "student_form.html", {'form':passwardForm})
    else:
        passwardForm = form.passward_valid()
    return render(request, "student_form.html", {'form':passwardForm})
