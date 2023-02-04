"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
from __future__ import annotations
from typing import Dict, Any
from dataclasses import dataclass
import requests
import datetime
import aiohttp
import json
import asyncio
#! usr/bin/env/python3
"""
TODO: Docstring to describe what this file does
"""
__author__ = "Korben Tompkin, Kayla Barker and Cheuk Pui Lam"
__licence__ = "MPL 2.0"
__version__ = "0.0.1"


API_LINK = "https://ucsc.cc/api"


async def async_pull(testing=False) -> dict:
    """Pulls current api data (asyncronously)

    Args:
        testing (bool, optional): Defines whether testing is in progress. Defaults to False.

    Returns:
        dict: pulled json file
    """
    if testing:
        return json.loads(open("apioutputs.json").read())
    async with aiohttp.ClientSession() as session:
        async with session.get(API_LINK) as resp:
            return await resp.json()


def sync_pull(testing=False) -> dict:
    """Pulls current api data syncronously

    Args:
        testing (bool, optional): Defines whether testing is in progress. Defaults to False.

    Returns:
        dict: pulled json file
    """
    if testing:
        return json.loads(open("apioutputs.json").read())
    return requests.get(API_LINK).json()


@dataclass
class Meal:
    """Class for keeping track of each meal"""
    name: str
    date: datetime.date
    tags: List[str]
    location: str
    category: str
    chow_time: str  # options are Breakfast,Lunch, Dinner,Late Night

    def __str__(self) -> str:
        return f"{self.name}"


def get_data() -> AllData:
    return MealData.from_api(sync_pull(testing=False))


class MealData(list):
    def __init__(self, data=list[Meal]) -> None:
        super().__init__(data)

    @classmethod
    def from_api(cls, data: List[Dict]) -> MealData:
        """Converts data into Mealdata

        Args:
            data (List[Dict]): pulled data

        Returns:
            MealData: MealData Object
        """
        r = []
        for days in data:
            curr_date = datetime.datetime.strptime(
                days['date'], "%Y-%m-%dT%H:%M:%S").date()
            for halls in days['halls']:
                curr_hall = halls['name']
                for m in halls['meals']:
                    curr_time = m['meal']
                    for c in m['cats']:
                        curr_category = c['cat']
                        for foods in c['foods']:
                            r.append(Meal(
                                name=foods['name'],
                                date=curr_date,
                                tags=list(foods['legend'].keys()),
                                location=curr_hall,
                                category=curr_category,
                                chow_time=curr_time))
        return MealData(r)

    def get_day(self, offset=0) -> MealData:
        target_day = datetime.date.today() + datetime.timedelta(days=offset)
        return MealData(filter(lambda x: x.date == target_day, self))

    def get_name(self, name: str) -> MealData:
        return MealData(filter(lambda x: x.name == name, self))

    def get_tags(self, tags: str) -> MealData:
        return MealData(self)
