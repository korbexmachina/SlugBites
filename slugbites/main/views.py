from django.shortcuts import render
from django.http import HttpResponse
from .models import foodItem
from api import get_data
# Create your views here.

def index(response) -> HttpResponse:
    return render(response, "main/base.html", {})

def food(response) -> HttpResponse:
    ls = get_data() # This should be a list of all food items int the database
    return render(response, "main/food.html", {"food":ls}) # This should display said items