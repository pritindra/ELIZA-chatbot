import requests
import json

API_KEY = '3b520d2fdc2044e9b22939eeb652a22d'

def newsbykeyword(key):

    r = requests.get('https://newsapi.org/v2/everything?q={key}&apiKey={API_KEY}')
    if status_code == 200:
        data = r.json()
        article = data.articles[0]
        text = f"Author: {article['author']} \nTitle: {article['title']} \nDescription: {article['description']} \nUrl: {article['url']} \nPublished: {article['publishedAt']} \nContent: {article['content']}"
    else:
        text = 'Sorry, could not receive the results..'
    return text

def newsbycategory(key,category):
    pass

def newsbycountry(key,coun):
    pass