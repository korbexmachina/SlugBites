"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import foodItem
from meal_api import get_data
# Create your views here.

def index(response) -> HttpResponse:
    return render(response, "main/base.html", {})

def food(response) -> HttpResponse:
    ls = get_data() # This should be a list of all food items int the database
    return render(response, "main/food.html", {"food":ls}) # This should display said items