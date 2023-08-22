#from functools import reduce
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
Personajes = ['Arstanselmy','Aegonn','Nnonno','Valkyrion','Walle','Sendarick']
server = 'https://raider.io/characters/us/ragnaros/'

direcciones = list()
for i in Personajes:
    direcciones.append(server+i)
dfn =list()


for i in direcciones:
    page = requests.get(i)
    soup = BeautifulSoup(page.text, 'lxml')

    #apuntando a la tabla en el codigo html
    table = soup.find('table', {
        'class': 'slds-table slds-table--striped slds-no-row-hover rio-guild-details-table slds-max-small-table'})
    #creando los encabezados del dataframe
    headers = [i.replace(server,""),'Reforzado','Tyranico',"Rating","Best Time","Best Affixes","World","Region"]
    df = pd.DataFrame(columns = headers)

    #obteniendo datos en cada td de cada tr
    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
    #dropeando las columnas que no necesito
    df = df.drop(columns=["Rating", "Best Time", "Best Affixes", "World", "Region"])

    #reemplazando letras malas y +
    #df = df.replace(dungeonbad, '', regex=True)
    # Suponiendo que df es tu DataFrame de pandas
    #df['Reforzado'] = df['Reforzado'].str.replace('+', '')
    #df['Tyranico'] = df['Tyranico'].str.replace('+', '')


    print(df)

# merge all DataFrames into one
#final_df = reduce(lambda left, right: pd.merge(left, right, on=['Dungeon'],
#                                                   how='outer'), dfs)

#final_df.to_csv('todo.csv', index=False)





