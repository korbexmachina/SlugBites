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

from typing import Dict


API_LINK = "https://ucsc.cc/api"


async def pull(testing=False) -> dict:
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


@dataclass
class Meal:
    """Class for keeping track of each meal"""
    name: str
    date: datetime.date
    tags: List[str]
    location: str
    time: str  # options are Breakfast,Lunch, Dinner,Late Night
