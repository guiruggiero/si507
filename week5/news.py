#news.py
from secrets import *
import requests

# gets headlines for today's news
def fetch_top_headlines(category=None):
    baseurl = 'https://newsapi.org/v2/top-headlines'
    params={'country': 'us'}
    if category is not None:
        params['category'] = category
    params['apiKey'] = newsapi_key
    return requests.get(baseurl, params).json()

def get_headlines(results_dict):
    results = results_dict['articles']
    headlines = []
    for r in results:
        headlines.append(r['title'])
    return headlines

science_list_json = fetch_top_headlines('science')
headlines = get_headlines(science_list_json)
for h in headlines:
    print(h)
