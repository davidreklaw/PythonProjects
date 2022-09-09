"""
Web scraping Men's Track and Field World Records using beautiful soup
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re

__author__ = "David Walker"
__version__ = "09/09/2022"
__pylint__ = "2.12.2"

def strip(info):
    info.replace("<td>", "")
    info.replace("</td>", "")
    if info == "":
        info = 'N/A'
    return info

if __name__ == '__main__':
     
    URL = "https://trackandfieldnews.com/records/mens-world-records/"
    result = requests.get(URL).text
    doc = BeautifulSoup(result, "html.parser")

    records = {}

    notes = doc.find(text = re.compile("^[(]A[)]\s[=]\S*"))
    records["Notes"] = notes

    trs = doc.find_all("tr", {"class": "recordline"})

    for tr in trs:
        event, mark, athlete, location, date = tr.contents[1::2]
        event = strip(event.text)
        mark =strip(mark.text)
        athlete = strip(athlete.text)
        location = strip(location.text)
        date = strip(date.text)
        records[event] = [mark, athlete, location, date]
        
    print(records)