from functools import reduce
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
Personajes = ['Arstanselmy','Engenieer','Leut','Nnonno','Sinpossio','Thúnderbolt','Valkyrion','Walle','Sendarick','Yyevuj','Redemers']
server = 'https://raider.io/characters/us/ragnaros/'
dungeonbad= ['YARD','UPPR','ID','LOWR','GD','WORK','GMBT','SD','STRT','SOA']


direcciones = list()
for i in Personajes:
    direcciones.append(server+i)
dfn =list()


for i in direcciones:
    page = requests.get(i)
    soup = BeautifulSoup(page.text, 'lxml')

    #obteniendo la tabla
    table = soup.find('table', {
        'class': 'slds-table slds-table--striped slds-no-row-hover rio-guild-details-table slds-max-small-table'})
    headers = [i.replace(server,""),'Reforzado','Tyranico',"Rating","Best Time","Best Affixes","World","Region"]
    df = pd.DataFrame(columns = headers)

    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
    df = df.drop(columns=["Rating", "Best Time", "Best Affixes", "World", "Region"])

    #reemplazando letras malas y +
    df = df.replace(dungeonbad, '', regex=True)
    df['Reforzado'] = df['Reforzado'].str.replace('+', '', regex=True)
    df['Tyranico'] = df['Tyranico'].str.replace('+', '', regex=True)

    # para guardar en archivo csv
    # imprimir remplazando el server
    #df.to_csv(i.replace(server,"")+'.csv',index=False)

    #para seleccionar los menos a 20
    #select_prod1 = df.loc[df['Tyranico'] < '20']
    #select_prod2 = df.loc[df['Reforzado'] < '20']
    #final_df = pd.merge(select_prod1, select_prod2, how="outer")
    #select_prod1 = df.loc[(df['Tyranico'] < '20') | (df['Reforzado'] < '20')]
    #select_prod1 = df.loc[(df['Reforzado'] < '20')]
    print(df)





    #print(df)




    #dfs.append(dfverdad1)

# merge all DataFrames into one
#final_df = reduce(lambda left, right: pd.merge(left, right, on=['Dungeon'],
#                                                   how='outer'), dfs)

#final_df.to_csv('todo.csv', index=False)




