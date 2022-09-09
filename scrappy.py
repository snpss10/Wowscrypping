from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
Personajes = ['Arstanselmy','Walle','Valkyrion','Leut','Sinpossio','Engenieer','Nnonno','Thúnderbolt']
server = 'https://raider.io/characters/us/ragnaros/'

dir = '.csv'
toxml = list()
for i in Personajes:
    toxml.append(i+dir)

direcciones = list()
for i in Personajes:
    direcciones.append(server+i)
dfn =list()

print(toxml)