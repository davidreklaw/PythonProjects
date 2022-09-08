"""
Tutorial following Tech With Time vide:

Beautiful Soup 4 Tutorial #3 - Navigating The HTML Tree

Link:
https://www.youtube.com/watch?v=lC6mucyD17k
"""

import requests
from bs4 import BeautifulSoup

__author__ = "David Walker"
__version__ = "Web Scraping Tutorial"
__pylint__ = "2.12.2"


if __name__ == '__main__':

    URL = "https://coinmarketcap.com/"
    result = requests.get(URL).text
    doc = BeautifulSoup(result, "html.parser")

    tbody = doc.tbody

    trs = tbody.contents

    prices = {}

    for tr in trs:
        name, price = tr.contents[2:4]
        try:
            fixed_name = name.p.string
            fixed_price = price.a.string
        except AttributeError:
            test = tr.findChildren()[4].findChildren()[2]
            fixed_name = test.string
            fixed_price = tr.findChildren()[-3].text
        prices[fixed_name] = fixed_price

    print(prices)
