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
    return render(response, "main/home.html", {})


def food(response) -> HttpResponse:
    # Displays all possible menu items
    return render(response, "main/food.html", {"food": food_data.full_menu()})


def currentmeal(response) -> HttpResponse:
    current_meal_data = food_data.current_meals()
    d = {}
    for items in current_meal_data:
        if items.location in d:
            d[items.location].append(items)
            continue
        d[items.location] = [items]
    return render(response, "main/currentmeal.html", {"meals": d})


def search(response) -> HttpResponse:
    print(response.GET)
    results = food_data.search(response.GET['search'])
    print(results)
    return render(response, "main/searchresults.html", {"meals": results})
    pass
