import requests
import json
# API KEY = 3b520d2fdc2044e9b22939eeb652a22d

def All_Continents():
    r = requests.get('https://corona.lmao.ninja/v2/continents?yesterday=true&sort')
    if r.status_code == 200:
        data1 = r.json()
        text = f""
        for i in range(6):
            data = data1[i]
            text = text + f"__Covid updates of yesterday__\n\nContinent:*{data['continent']}* \n\nCases: *{data['cases']}* \n\nDeaths: *{data['deaths']}* \n\nRecovered: *{data['recovered']}* \n\nActive cases: *{data['active']}* \n\nCritical cases: *{data['critical']}*"
    else:
        text = 'Sorry, could not receive the results..'
    return text

def Specific_Continent(cont):
    r = requests.get('https://corona.lmao.ninja/v2/continents/:{cont}?yesterday&strict')

    if r.status_code == 200:
        data = r.json()
        text = f"__Covid updates of {data['continent']} for yesterday__ \n\nCases: *{data['cases']}* \n\nDeaths: *{data['deaths']}* \n\nRecovered: *{data['recovered']}* \n\nActive cases: *{data['active']}* \n\nCritical cases: *{data['critical']}*"
    else:
        text = 'Sorry, could not receive the results..'

    return text

def Specific_Country(coun):
    r = requests.get('https://corona.lmao.ninja/v2/countries/:{coun}?yesterday=true&strict=true&query')

    if r.status_code == 200:
        data = r.json()
        text = f"__Covid updates of {data['country']} for yesterday__ \n\nCases: *{data['cases']}* \n\nDeaths: *{data['deaths']}* \n\nRecovered: *{data['recovered']}* \n\nActive cases: *{data['active']}* \n\nCritical cases: *{data['critical']}* \n\nTests: *{data['tests']}*"
    else:
        text = 'Sorry, could not receive the results..'

    return text


def History_Country(coun,days):
    r = requests.get('https://corona.lmao.ninja/v2/historical/:{coun}?lastdays={days}')

    if r.status_code == 200:
        data = r.json()

        text = f"__Covid updates of {data['country']} for {days} days  \n\nCases: *{case['cases'] for case in data['timeline']}* \n\nDeaths: *{d['deaths'] for d in data['timeline']}* \n\nRecovered: *{recover['recovered'] for recover in data['timeline']}*"
    else:
        text = 'Sorry, could not receive the results..'
    return text