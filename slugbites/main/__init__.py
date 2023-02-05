"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
from __future__ import annotations
from typing import Dict, Any, List, Union
from dataclasses import dataclass
import requests
import datetime
import aiohttp
import json
import asyncio
from zoneinfo import ZoneInfo
from .dining_hall_times import times
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
    chow_time: str  # options are Breakfast,Lunch, Dinner,Late Night
    category: str

    def __str__(self) -> str:
        return f"{self.name}"

    def json(self) -> Dict[str, Union[str, List]]:
        return {
            "name": self.name,
            "date": str(self.date),
            "tags": self.tags,
            "location": self.location,
            "chow_time": self.chow_time,
            "category": self.category
        }


class MealData(list):
    flags = {'treenut', 'shellfish', 'vegan', 'veggie', 'beef', 'soy', 'gluten',
             'halal', 'unknown', 'milk', 'nuts', 'pork', 'fish', 'alcohol', 'sesame', 'eggs'}
    # only *gluten is flag gluten free
    locations = {'Crown/Merrill', 'College Nine/John R Lewis',
                 'Porter/Kresge', 'Cowell/Stevenson'}

    def __init__(self, data: List[Meal] = []) -> None:
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
                                chow_time=curr_time,
                                category=curr_category))
        return MealData(r)

    def get_day(self, offset=0) -> MealData:
        """Gets all data from certain day

        Args:
            offset (int, optional): day difference from "today". Defaults to 0.

        Returns:
            MealData: meal list
        """
        target_day = (datetime.datetime.now(tz=ZoneInfo(
            "America/Los_Angeles")) + datetime.timedelta(days=offset)).date()
        return MealData(filter(lambda x: x.date == target_day, self))

    def get_name(self, name: str) -> MealData:
        """Gets only meals with the name equal to name

        Args:
            name (str): meal name we're looking for

        Returns:
            MealData: meal list
        """
        return MealData(filter(lambda x: x.name == name, self))

    def get_names(self, names: List[str]) -> MealData:
        """Get meals with the name equal to any of the names

        Args:
            names (List[str]): names that are wanted

        Returns:
            MealData: meal list
        """
        r = MealData()
        for i in names:
            r.extend(self.get_name(i))
        return r

    def get_tags(self, tags: List[str]) -> MealData:
        """Get only meals with all tags within tags

        Args:
            tags (List[str]): list of tags we want

        Returns:
            MealData: meal lsit
        """
        return MealData(filter(lambda x: all(i in x.tags for i in tags), self))

    def get_location(self, location: List[str]) -> MealData:
        """Get only meals at given dining halls

        Args:
            location (List[str]): list of dining halls

        Returns:
            MealData: meal list
        """
        return MealData(filter(lambda x: x.location in location, self))

    def get_chow_time(self, time: str) -> MealData:
        """Get only meals at chow time

        Args:
            time (str): chow time, options are Breakfast, Lunch, Dinner, and Late Night

        Returns:
            MealData: meal list
        """
        return MealData(filter(lambda x: x.chow_time == time, self))

    def get_category(self, category: List[str]) -> MealData:
        """Get only meals at category

        Args:
            category (List[str]): list of categories we are going to write

        Returns:
            MealData: meal data
        """
        return MealData(filter(lambda x: x.category in category, self))

    def ignore_tags(self, tags: List[str]) -> MealData:
        """Ignores meals with any tags within

        Args:
            tags (List[str]): tags to be ignored

        Returns:
            MealData: meal data
        """
        return MealData(filter(lambda x: not any(i in x.tags for i in tags), self))

    def ignore_category(self, category: List[str]) -> MealData:
        """Ignores meals with any categories given

        Args:
            category (List[str]): categories to be ignored

        Returns:
            MealData: meal data
        """
        return MealData(filter(lambda x: not x.category in category, self))

    def full_menu(self) -> Dict[str, List[str]]:
        """Returns the full menu

        Returns:
            Dict[str, List[str]]: Dictionary with breakfast and everything else
        """
        r = {"Breakfast": [], "Everything Else": []}
        for i in self:
            if i.chow_time == "Breakfast" and i.name not in r['Breakfast']:
                r['Breakfast'].append(i.name)
            elif i.chow_time != "Breakfast" and i.name not in r['Everything Else']:
                r['Everything Else'].append(i.name)
        r['Breakfast'].sort()
        r['Everything Else'].sort()
        return r

    def search(self, s: str) -> MealData:
        """Searches for a match string

        Args:
            s (str): string

        Returns:
            MealData: meal data
        """
        return MealData(filter(lambda x: s.lower() in x.name.lower(), self))

    def current_meals(self, t: datetime.Datetime = datetime.datetime.now(tz=ZoneInfo("America/Los_Angeles"))) -> MealData:
        """Gets current/next meal of today

        Args:
            t (datetime.Datetime, optional): datetime object. Defaults to datetime.datetime.now().

        Returns:
            MealData: Mealdata list
        """
        r = MealData()
        day_info = times[t.weekday()]
        time_info = t.hour * 2 + t.minute//30
        offset = (
            t.date()-datetime.datetime.now(tz=ZoneInfo("America/Los_Angeles")).date()).days
        for colleges in day_info:
            for ts, meals in day_info[colleges].items():
                if time_info not in ts:
                    continue
                elif meals not in ['Closed', "Limited Options"]:
                    r.extend(self.get_chow_time(
                        meals).get_location(colleges).get_day(offset))
                elif meals == "Closed" and time_info < 14 or meals == "Limited Options" and time_info < 23:
                    r.extend(self.get_chow_time("Breakfast").get_location(
                        colleges).get_day(offset))
                elif meals == "Limited Options":
                    r.extend(self.get_chow_time("Lunch").get_location(
                        colleges).get_day(offset))
        return r

    def format_to_meals(self) -> Dict[str, Dict]:
        d = {}
        for items in self:
            if items.chow_time in d:
                d[items.chow_time].append(items)
            else:
                d[items.chow_time] = [items]
        return d

    def format_to_colleges(self) -> Dict[str, Dict]:
        d = {}
        for items in self:
            if items.location in d:
                d[items.location].append(items)
                continue
            d[items.location] = [items]
        return d

    def format_to_day_meal(self) -> Dict[str, Dict]:
        d = {}
        for items in self:
            fstr = f"{items.date} {items.chow_time}"
            if fstr in d:
                d[fstr].append(items)
            else:
                d[fstr] = [items]
        return d


def get_data(testing=False) -> MealData:
    return MealData.from_api(sync_pull(testing=testing))
