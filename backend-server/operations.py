#!/usr/bin/env python
"""Backend Server Operations"""
from datetime import datetime
from pickle import loads as pickle_loads, dumps as pickle_dumps
from common.mongodb_news import news_table
from common.top_news_config import config
from common.user_news_cache_redis import redis_client
from common.click_log_queue import send_click_log
from common.recommendation_client import getPreferenceForUser

backend_server_cfg = config['backendServer']
NEWS_PAGE_SIZE =  backend_server_cfg["newsPageSize"]
NEWS_TOTAL_LIMIT = backend_server_cfg["newsTotalLimit"]
USER_NEWS_TIME_OUT = backend_server_cfg["userNewsTimeOut"]

PUBLISH_AT_W = 0.05
CATEGORY_W = 10
COUNTRY_W = 10
LANGUAGE_W = 20
KEYWORDS_W = 5

def sort_news(preference):
    now = datetime.utcnow()
    def news_sort(news):
        prob = 0
        if 'publishedAt' in news:
            prob += (news['publishedAt'] - now).total_seconds() * PUBLISH_AT_W
        if 'category' in news:
            prob += preference['category'][news['category']] * CATEGORY_W
        if 'country' in news:
            prob += preference['country'][news['country']] * COUNTRY_W
        if 'language' in news:
            prob += preference['language'][news['language']] * LANGUAGE_W
        if 'keywords' in news:
            preference_keywords = preference['keywords']
            p1 = p2 = 0
            for _,v in preference_keywords:
                p1 += v
            for keyword in news['keywords']:
                if keyword in preference_keywords:
                    p2 += preference_keywords[keyword]
            if p1 != 0:
                prob += KEYWORDS_W * p2 / p1
        return prob
    return news_sort


def _delete_text_and_from_bson_to_json(sliced_news):
    for news in sliced_news:
        del news['text']
        del news['_id']
        news['publishedAt'] = news['publishedAt'].isoformat(timespec='seconds') + 'Z'
    return sliced_news

def more_news_for_user(user_id, page_num):
    page_num = int(page_num)
    
    begin_index = page_num * NEWS_PAGE_SIZE
    end_index = begin_index + NEWS_PAGE_SIZE

    news_digests = redis_client.get(user_id)
    if news_digests is None:
        return clear_news_for_user(user_id)
    news_digests = pickle_loads(news_digests)
    sliced_news_digest = news_digests[begin_index:end_index]
    sliced_news = list(news_table.find({'digest': {'$in': sliced_news_digest}}))
    return _delete_text_and_from_bson_to_json(sliced_news)


def clear_news_for_user(user_id):
    total_news = list(news_table.find().sort([('publishedAt', -1)]).limit(NEWS_TOTAL_LIMIT))
    user_preference = getPreferenceForUser(user_id)
    total_news.sort(key=sort_news(user_preference), reverse=True)
    news_digests = [x['digest'] for x in total_news]
    redis_client.set(user_id, pickle_dumps(news_digests), ex=USER_NEWS_TIME_OUT)
    sliced_news = total_news[0:NEWS_PAGE_SIZE]
    return _delete_text_and_from_bson_to_json(sliced_news)

def log_news_click_for_user(user_id, news_digest):
    print('click-log: ', user_id)
    send_click_log({
        'userId': user_id,
        'newsDigest': news_digest,
        'timestamp': datetime.utcnow().isoformat()})
    pass
