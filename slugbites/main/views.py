from django.shortcuts import render
from django.http import HttpResponse
from .models import foodItem
# Create your views here.

def index(response) -> HttpResponse:
    return render(response, "main/base.html", {})

def food(response) -> HttpResponse:
    ls = str(foodItem) # This should be a list of all food items int the database
    return render(response, "main/food.html" %(ls), {}) # This should display said items