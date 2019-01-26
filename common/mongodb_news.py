#!/bin/env python
from .top_news_config import config
from pymongo import MongoClient

_mongo_news_cfg = config['mongoDBNews']

client = MongoClient('%s:%d' % (_mongo_news_cfg['host'], _mongo_news_cfg['port']))
news_db = client[_mongo_news_cfg['db']]
news_table = news_db[_mongo_news_cfg['newsTableName']]
