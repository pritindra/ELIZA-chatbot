import requests
import json

def All_Continents():
    r = requests.get('https://corona.lmao.ninja/v2/continents?yesterday=true&sort')
    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'

def Specific_Continent(cont):
    r = requests.get('https://corona.lmao.ninja/v2/continents/:{cont}?yesterday&strict')

    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'

def Specific_Country(coun):
    r = requests.get('https://corona.lmao.ninja/v2/countries/:{coun}?yesterday=true&strict=true&query')

    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'


def History_Country(coun,days):
    r = requests.get('https://corona.lmao.ninja/v2/historical/:{coun}?lastdays={days}')

    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'