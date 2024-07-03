from django.shortcuts import render
import datetime

def home(request):
    d = {'name':'robiul',
         'roll': 2108015,
         'age': 2,
         'list':['python','is','a','magic','for','world'],
         'birthday':datetime.datetime.now(),
         'course':[
             {
                 'id':1,
                 'name':"python",
                 'free':1000
             },
             {
                 'id':2,
                 'name':"Django",
                 'free':10000
             },
             {
                 'id':3,
                 'name':"C++",
                 'free':3000
             }
         ],
         }
    return render(request, "first_app/home.html",d)
