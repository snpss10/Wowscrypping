from functools import reduce
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://coalicionciudadana.pe'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


table = soup.find('table', {'class':'slds-table slds-table--striped slds-no-row-hover rio-guild-details-table slds-max-small-table'})
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data