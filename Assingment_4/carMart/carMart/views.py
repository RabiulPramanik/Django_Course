from django.shortcuts import render
from car.models import CarModel
from brand.models import BrandModel


def home(request, brand_slug = None):
    car = CarModel.objects.all()
    brand = BrandModel.objects.all()
    if brand_slug is not None:
        bd = BrandModel.objects.get(slug = brand_slug)
        car = CarModel.objects.filter(brand = bd)
    return render(request, "home.html", {'car':car, 'brand':brand})