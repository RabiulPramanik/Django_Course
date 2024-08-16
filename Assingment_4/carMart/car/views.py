from django.shortcuts import render, redirect
from .models import CarModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from comment.models import CommentModel
from comment.form import CommentForm
from django.views.generic import DetailView
from django.urls import reverse_lazy

@login_required
def car_details(request, id):
    car = CarModel.objects.get(pk = id)
    comment = CommentModel.objects.filter(car = car)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.car = car
            form.save()
            return redirect("detailspage", id = car.id)
    else:
        form = CommentForm()
    return render(request, "details.html", {'car':car, 'comment':comment, 'form':form, 'type':'Write Your Comment'})

@method_decorator(login_required, name="dispatch")
class car_detailsView(DetailView):
    model = CarModel
    template_name = "details.html"
    pk_url_kwarg = 'id'
    context_object_name = 'car'
    

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return self.get(request, *args, **kwargs)
        else:
            return redirect("detailspage", id = car.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comment"] = CommentModel.objects.filter(car = self.get_object())
        context["type"] = 'Write your comment'
        return context
    
