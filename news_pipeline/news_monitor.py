#!/bin/env python
import hashlib
import random
from common.top_news_config import config
from common.cloudAMQP_client import CloudAMQPClient
from common.scrape_task_queue import send_scrape_task as send_scrape_task
from common.news_api_client import get_news
from common.news_monitor_dedupe_redis import redis_client

news_api_cfg = config['newsAPI']
NEWS_API_URL = news_api_cfg['url'] + news_api_cfg['endpoint']
SAME_NEWS_TIME_OUT = config['newsMonitor']['sameNewsTimeOut']

def handle_message(news):
    news_digest = hashlib.md5(news['url'].encode()).hexdigest()
    if redis_client.get(news_digest) is not None:
        return 0
    news['digest'] = news_digest
    redis_client.set(news_digest, '0', ex=SAME_NEWS_TIME_OUT)
    send_scrape_task(news)
    return 1

def run():
    news_num = 0
    news_total = 0
    for category in news_api_cfg['categories']:
        for country in news_api_cfg['countries']:
            num = 0
            news_list = []
            try:
                news_list = get_news(NEWS_API_URL, category, country, random.choice(news_api_cfg['keys']))
            except Exception as e:
                print('News-API error! %r.' % e.args[0])
                return
            for news in news_list:
                num += handle_message(news)
            print('Get %d, effective %d' % (len(news_list), num))
            news_num += num
            news_total += len(news_list)
    print('Total Get %d effective %d' % (news_total, news_num))

if __name__ == "__main__":
    run()