#!/bin/env python
import os
import json

CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

config = None
with open(CONFIG_FILE, 'r') as cfgf:
    config = json.load(cfgf)

mongodb_user_cfg = config["mongoDBUser"]
mongodb_news_cfg = config["mongoDBNews"]
mongodb_preference_cfg = config["mongoDBPreference"]
news_monitor_dedupe_redis_cfg = config["newsMonitorDedupeRedis"]
user_news_cache_redis_cfg = config["userNewsCacheRedis"]
scrape_task_queue_cfg = config["scrapeTaskQueue"]
dedupe_task_queue_cfg = config["dedupeTaskQueue"]
click_log_queue_cfg = config["clickLogQueue"]
web_server_cfg = config["webServer"]
backend_server_cfg = config["backendServer"]
recommendation_server_cfg = config["recommendationServer"]
news_topic_server_cfg = config["topicProvideServer"]
news_monitor_cfg = config["newsMonitor"]
news_fetcher_cfg = config["newsFetcher"]
news_deduper_cfg = config["newsDeduper"]
jwt_secret = config["jwtSecret"]
news_api_cfg = config["newsAPI"]
click_log_processor_cfg = config["clickLogProcessor"]
news_topic_model_cfg = config["newsTopicModel"]

if __name__ == '__main__':
    print(config)
