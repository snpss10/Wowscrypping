from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://raider.io/characters/us/ragnaros/Arstanselmy'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Piedras
eq = soup.find_all('span', class_='fresnel-greaterThan-sm')
eq.pop(0)
piedras = list()
for i in eq:
    piedras.append(i.text)
piedrastru= list()
piedrastru = piedras[:-2]

# Puntuacion
eq1 = soup.find_all('span', class_='slds-text-heading--small')
puntaje = list()
for i in eq1:
    puntaje.append(i.text)

correcto = list()
for i in puntaje:
    correcto.append(i.replace("+", ""))

pares = list()
impares = list()
contador = 0
for i in correcto:
     if contador % 2 == 0:
         impares.append(int(i))
     else:
         pares.append(int(i))
     contador += 1

d = {'dungeon': piedrastru, 'Forticado': impares, 'Tyranico': pares}
df = pd.DataFrame(data=d)



print(piedrastru)
print(correcto)
print(impares)
print(pares)
print(df)



