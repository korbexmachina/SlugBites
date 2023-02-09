"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import foodItem
from . import get_data

food_data = get_data()

# Views

def index(response) -> HttpResponse:
    return HttpResponseRedirect("/home")


def home(response) -> HttpResponse:
    curr = food_data.get_day().get_category("Entrees")
    c9 = curr.get_location('College Nine/John R Lewis').format_to_meals()
    cow = curr.get_location("Cowell/Stevenson").format_to_meals()
    cro = curr.get_location("Crown/Merrill").format_to_meals()
    por = curr.get_location("Porter/Kresge").format_to_meals()
    return render(response, "main/home.html", {"C9": c9, "COW": cow, "CRO": cro, "POR": por})


def food(response) -> HttpResponse:
    # Displays all possible menu items
    return render(response, "main/food.html", {"food": food_data.full_menu()})


def currentmeal(response) -> HttpResponse:
    return HttpResponseRedirect("/home")


def search(response) -> HttpResponse:
    # print(response.GET)
    results = food_data.search(response.GET['search'])
    c9 = results.get_location('College Nine/John R Lewis').format_to_day_meal()
    cow = results.get_location("Cowell/Stevenson").format_to_day_meal()
    cro = results.get_location("Crown/Merrill").format_to_day_meal()
    por = results.get_location("Porter/Kresge").format_to_day_meal()
    print(results)
    return render(response, "main/searchresults.html", {"C9": c9, "COW": cow, "CRO": cro, "POR": por})
    pass
