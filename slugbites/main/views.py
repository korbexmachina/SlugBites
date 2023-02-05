"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import foodItem
from . import get_data, current_meals

food_data = get_data()
current_meal_data = current_meals()

# Create your views here.


def index(response) -> HttpResponse:
    return HttpResponseRedirect("/home")


def home(response) -> HttpResponse:
    return render(response, "main/home.html", {})


def food(response) -> HttpResponse:
    # Displays all possible menu items
    return render(response, "main/food.html", {"food": food_data.full_menu()})


def currentmeal(response) -> HttpResponse:
    return render(response, "main/currentmeal.html", {})