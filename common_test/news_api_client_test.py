#!/bin/env python
import random
from common.news_api_client import get_news
from common.top_news_config import config

def test_basic():
    news_cfg = config['newsAPI']
    news_list = get_news(
        news_cfg['url'] + news_cfg['endpoint'],
        random.choice(news_cfg['categories']),
        random.choice(news_cfg['countries']),
        random.choice(news_cfg['keys']))
    print(news_list)
    assert len(news_list) > 0
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()
