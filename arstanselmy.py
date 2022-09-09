from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://raider.io/characters/us/ragnaros/Arstanselmy'
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
    correcto.append(i.replace('\xa0', "").replace('   (Score: 3,004.9)',""))

df = pd.DataFrame(columns = correcto)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data


dfverdad1 = df.drop(columns=["Rating","Best Time","Best Affixes","World","Region"])

##################################################data frame 2

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
    correcto.append(i.replace('\xa0', "").replace('   (Score: 2,748.7)',""))

df = pd.DataFrame(columns = correcto)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data


dfverdad2 = df.drop(columns=["Rating","Best Time","Best Affixes","World","Region"])

dfverdad3 = dfverdad1.merge(dfverdad2, left_on='Dungeon', right_on='Dungeon')
print(dfverdad3)

#dfverdad3.to_csv('todo1.csv', index=False)
dfverdad3.to_csv('todo3.csv', index=False)

