from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def obtener_final_df():
    Personajes = ['Arstanselmy', 'Aegonn', 'Nnonno', 'Valkyrion', 'Walle', 'Sendarick']
    server = 'https://raider.io/characters/us/ragnaros/'

    dfs = []  # Lista para almacenar los DataFrames individuales

    for i in Personajes:
        direcciones = [server + i]
        for direccion in direcciones:
            page = requests.get(direccion)
            soup = BeautifulSoup(page.text, 'lxml')

            # Apuntando a la tabla en el código HTML
            table = soup.find('table', {
                'class': 'slds-table slds-table--striped slds-no-row-hover rio-guild-details-table slds-max-small-table'})

            # Creando los encabezados del DataFrame
            headers = [i.replace(server, ""), 'Reforzado', 'Tyranico', "Rating", "Best Time", "Best Affixes", "World", "Region"]
            df = pd.DataFrame(columns=headers)

            # Obteniendo datos en cada td de cada tr
            for row in table.find_all('tr')[1:]:
                data = row.find_all('td')
                row_data = [td.text.strip() for td in data]
                length = len(df)
                df.loc[length] = row_data

            # Dropeando las columnas que no necesitas
            df = df.drop(columns=["Rating", "Best Time", "Best Affixes", "World", "Region"])

            # Reemplazando letras malas y +
            df['Reforzado'] = df['Reforzado'].str.replace('+', '')
            df['Tyranico'] = df['Tyranico'].str.replace('+', '')

            dfs.append(df)

    # Hacer merge de los DataFrames en uno solo
    final_df = pd.concat(dfs, axis=1)
    pd.set_option('display.max_columns', None)
    print(final_df)
    return final_df