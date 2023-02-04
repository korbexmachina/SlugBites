"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import foodItem
from . import get_data

food_data = get_data()

# Create your views here.

def index(response) -> HttpResponse:
    return HttpResponseRedirect("/home")

def home(response) -> HttpResponse:
    return render(response, "main/home.html", {"food": get_data()})

def food(response) -> HttpResponse:
    return render(response, "main/food.html", {"food":food_data.full_menu()}) # Displays all possible menu items