from bs4 import BeautifulSoup
import requests
import pandas as pd

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
            headers = ['Dungeons', 'R ' + i, 'T ' + i]
            df = pd.DataFrame(columns=headers)

            # Obteniendo datos en cada td de cada tr
            for row in table.find_all('tr')[1:]:
                data = row.find_all('td')
                row_data = [td.text.strip() for td in data]
                if len(row_data) >= 3:  # Asegurarse de que hay suficientes datos para agregar
                    df.loc[len(df)] = row_data[:3]  # Tomar solo los primeros 3 valores

            df = df.rename(columns={'R ' + i: 'Reforzado ' + i, 'T ' + i: 'Tyranico ' + i})
            dfs.append(df)

    # Hacer merge de los DataFrames en uno solo
    final_df = pd.DataFrame()
    for df in dfs:
        if final_df.empty:
            final_df = df
        else:
            final_df = final_df.merge(df, on='Dungeons', how='outer')

    # Imprimir el DataFrame final combinado
    pd.set_option('display.max_columns', None)
    print(final_df)
    return final_df



