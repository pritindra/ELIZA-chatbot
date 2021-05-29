import requests
import json
import time


d = time.strftime("%d-%m-%Y")

def findbydist(id_msg):
    r = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/{id_msg}')
    if r.status_code == 200:
        data = r.json()
        text = f'{data}'
    else:
        text = 'I could not receive the results at this time, sorry.'

def findbypin(pin_msg):
    payload = {'pincode':pin_msg, 'date':d}
    r = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin',params=payload)
    if r.status_code == 200:
        data = r.json()
        text = f'{data}'
    else:
        text = 'I could not receive the results at this time, sorry.'
    

