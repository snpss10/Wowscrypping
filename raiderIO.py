from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://raider.io/characters/us/ragnaros/Walle'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup

#getting the table
table = soup.find('table', {'class':'slds-table slds-table--striped slds-no-row-hover rio-guild-details-table slds-max-small-table'})

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

#eliminando letras
correcto = list()
for i in headers:
    correcto.append(i.replace('\xa0', ""))

df = pd.DataFrame(columns = correcto)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data


dfverdad = df.drop(columns=["Rating","Best Time","Best Affixes","World","Region"])

#del correcto[3:8]
#print(correcto)
dfverdad.to_csv('arstanselmy1.csv', index=False)


