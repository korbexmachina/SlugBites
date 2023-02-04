from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response) -> HttpResponse:
    return HttpResponse("<h1>Hello world!<h1>")