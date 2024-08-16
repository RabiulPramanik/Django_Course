from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

def home(request):
    responce = render(request, "home.html")
    responce.set_cookie('name', 'Suborna')
    # responce.set_cookie('name', 'Robiul', max_age=10)
    responce.set_cookie('name', 'Robiul', expires=datetime.utcnow()+timedelta(days=7))
    return responce

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, "get.html", {'name':name})

def delete_cookie(request):
    responce = render(request, "del.html")
    responce.delete_cookie('name')
    return responce

def set_session(request):
    data = {
        'name':'Suborna',
        'age': 24,
        'language':'bangla',
    }
    request.session.update(data)
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    return render(request, "home.html")

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Gusht')
        age = request.session.get('age')
        request.session.modified = True
        return render(request, "get_session.html", {'name':name, 'age':age})
    else:
        return HttpResponse("Session time is Expired")

def delete_session(request):
    request.session.flush()
    return render(request, "del.html")
