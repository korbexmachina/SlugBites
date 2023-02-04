from django.shortcuts import render
from django.http import HttpResponse
from .models import foodItem
# Create your views here.

def index(response) -> HttpResponse:
    return HttpResponse("<h1>Hello world!<h1>")

def food(response) -> HttpResponse:
    ls = foodItem.all() # This should be a list of all food items int the database
    return HttpResponse("<h1>Food:<h1>" %(ls.name)) # This should display said items