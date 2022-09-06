# Web Scraping Examples

Examples python files of web scraping

## Instillation

The package manager [pip](https://pip.pypa.io/en/stable/) was used to install the necessary packages

The packages used are:

1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```bash
pip install beautifulsoup4
```

2. [Request](https://pypi.org/project/requests/)

```bash
pip install requests
```

3. [Regex](https://pypi.org/project/regex/)

```bash
pip install regex
```

## Coding Style and Guide Lines

These files follow [python coding guide lines](https://github.com/davidreklaw/PythonProjects/blob/main/UWG_Python_Style_Guide.txt) from coding roles given at the University of West Georgia, a copy of the guidelines is provided in this repo.

## Files

### Crypto.py

This file is following a [Tech With Tim Video](https://www.youtube.com/watch?v=lC6mucyD17k&t=517s) and uses [CodeMarketCap](https://coinmarketcap.com/) to get crypto prices

Challenges:
- After about 10 rows in the table data is stored in the html differently and had to be extracted differently. The video example only goes through the first 10