"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

from __future__ import annotations
#! usr/bin/env/python3
"""
TODO: Docstring to describe what this file does
"""
__author__ = "Korben Tompkin, Kayla Barker and Cheuk Pui Lam"
__licence__ = "MPL 2.0"
__version__ = "0.0.1"
import asyncio
import json
import aiohttp
import datetime
import requests
from dataclasses import dataclass

from typing import Dict


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

    def __str__(self) -> str:
        return f"{self.name}"


def get_data() -> AllData:
    return AllData(sync_pull())


class AllData:
    def __init__(self, data: List[Dict]) -> None:
        self.data = self.parse_data(data)
        print(len(self.data))

    def parse_data(self, data: List[Dict]) -> List[Meal]:
        """Parsing data from the api and outputs it as a list of meals

        Args:
            data (List[Dict]): datas

        Returns:
            List[Meal]: list of meals within the 7 day period
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
                        for foods in c['foods']:
                            r.append(Meal(
                                name=foods['name'],
                                date=curr_date,
                                tags=list(foods['legend'].keys()),
                                location=curr_hall,
                                chow_time=curr_time))
        return r

    def _get(tag: str) -> List[Meals]:
        pass

    def get_day(offset=0) -> List:
        pass
