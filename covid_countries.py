import requests
import json

def All_Continents():
    r = requests.get('https://corona.lmao.ninja/v2/continents?yesterday=true&sort')
    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'
    return text

def Specific_Continent(cont):
    r = requests.get('https://corona.lmao.ninja/v2/continents/:{cont}?yesterday&strict')

    if status_code == 200:
        data = r.json()
        text = f'__Covid updates of {data['continent']} for yesterday__ \n\nCases: *{data['cases']}* \n\nDeaths: *{data['deaths']}* \n\nRecovered: *{data['recovered']}* \n\nActive cases: *{data['active']}* \n\nCritical cases: *{data['critical']}*'
    else:
        text = 'Sorry, could not receive the results..'

    return text

def Specific_Country(coun):
    r = requests.get('https://corona.lmao.ninja/v2/countries/:{coun}?yesterday=true&strict=true&query')

    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'

    return text


def History_Country(coun,days):
    r = requests.get('https://corona.lmao.ninja/v2/historical/:{coun}?lastdays={days}')

    if status_code == 200:
        data = r.json()
        text = f'data'
    else:
        text = 'Sorry, could not receive the results..'
    return text