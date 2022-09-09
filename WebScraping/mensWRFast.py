"""
Web scraping Men's Track and Field World Records using beautiful soup
"""

import requests
import pandas as pd

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

    df = pd.read_html(URL)
    print(df)
    print()