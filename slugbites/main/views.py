from django.shortcuts import render
from django.http import HttpResponse
from .models import foodItem
# Create your views here.

def index(response) -> HttpResponse:
    return HttpResponse("<h1>Hello world!<h1>")

def v1(response0) -> HttpResponse:
    return HttpResponse("<h1>Success!<h1>")