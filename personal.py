from functools import reduce
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as npi
nick='Sinpossio'
url = 'https://raider.io/characters/us/ragnaros/'
urlnick = url + nick
dungeonbad= ['YARD','UPPR','ID','LOWR','GD','WORK','GMBT','SD','STRT','SOA']
page = requests.get(urlnick)
soup = BeautifulSoup(page.text, 'lxml')

headers = ['Dungeon','Reforzado','Tyranico',"Rating","Best Time","Best Affixes","World","Region"]
df = pd.DataFrame(columns = headers)

table = soup.find('table', {'class':'slds-table slds-table--striped slds-no-row-hover rio-guild-details-table slds-max-small-table'})
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data
df = df.drop(columns=["Rating","Best Time","Best Affixes","World","Region"])

#reemplazando letras malas y +
df = df.replace(dungeonbad,'', regex=True)
df['Reforzado'] = df['Reforzado'].str.replace('+', '', regex=True)
df['Tyranico'] = df['Tyranico'].str.replace('+', '', regex=True)

# para seleccionar los menos a 20
#select_prod1 = df.loc[(df['Tyranico']  < '20')|(df['Reforzado']  < '20')]
#select_prod1 = df.loc[(df['Tyranico']  < '20')]


print(df)


#union de los dataframes
#final_df =  pd.merge(select_prod1,select_prod2, how= "outer")

#print(select_prod1)




#dfverdad.to_csv('Leut.csv', index=False)