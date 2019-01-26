#!/bin/env python
from .top_news_config import config
from pymongo import MongoClient

_mongo_preference_cfg = config['mongoDBPreference']

client = MongoClient('%s:%d' % (_mongo_preference_cfg['host'], _mongo_preference_cfg['port']))
preference_db = client[_mongo_preference_cfg['db']]
preference_table = preference_db[_mongo_preference_cfg['preferenceTableName']]
