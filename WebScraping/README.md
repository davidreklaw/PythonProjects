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

4. [Pandas](https://pandas.pydata.org/)
```bash
pip install pandas
```

## Coding Style and Guide Lines

These files follow [python coding guide lines](https://github.com/davidreklaw/PythonProjects/blob/main/UWG_Python_Style_Guide.txt) from coding roles given at the University of West Georgia, a copy of the guidelines is provided in this repo.

## Files

### Crypto.py

This file is following a [Tech With Tim Video](https://www.youtube.com/watch?v=lC6mucyD17k&t=517s) and uses [CoinMarketCap](https://coinmarketcap.com/) to get crypto prices

Challenges:
- After about 10 rows in the table data is stored in the html differently and had to be extracted differently. The video example only goes through the first 10

### MensWorldRecords.py and MensWRFast.py

These two files do basically the same thing. They scrap a web sight of [Men's Track and Field World Records](https://trackandfieldnews.com/records/mens-world-records/) and pulls the records from multiple tables, for all track and field and even relay world record information. 

Challenges:
- The biggest challenge was the fact that there were multiple tables to pull information from unlike the previous script that was pulling information from just a single table. And since the different tables didn't have a summery tag or a differentiating tag for each table I had to get a little creative. 

Differences:
- Using **BeautifulSoup** and **Pandas**, is that Pandas uses can automatically pull all the tables separately and **all** of the information in those tables and displays it easily in the console. Also, for relay participants and splits for the athletes, Pandas pull that information when BeautifulSoup does not.