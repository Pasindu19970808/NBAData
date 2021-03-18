import bs4 as BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import re


url = "https://www.basketball-reference.com/leagues/NBA_2013_totals.html"
html_content = urllib.request.urlopen(url)
bsoup = BeautifulSoup.BeautifulSoup(html_content,'html.parser')
year_list = bsoup.find_all('table',{'id':'totals_stats'})[0].find_all('tbody')[0].find_all('tr',class_ = lambda x: x!= 'thead')

for row in year_list:
        row_result = list(map(lambda x: x.get_text(),row))