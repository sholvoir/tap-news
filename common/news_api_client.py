import requests
from json import loads as json_loads

def get_news(news_api_url, category, country, apiKey):
    params = {
        'category': category,
        'country': country,
        'apiKey': apiKey
    }

    print(params)
    res = json_loads(requests.get(news_api_url, params=params).content.decode())

    if res is None:
        raise Exception('System Error!')
    if res['status'] != 'ok':
        raise Exception(res)

    print('Total: %d, Get: %d.' % (res['totalResults'], len(res['articles'])))

    for news in res['articles']:
        news['category'] = category
        news['country'] = country
        source = news['source']
        news['source'] = source['id'] if source['id'] else source['name']
    
    return res['articles']
