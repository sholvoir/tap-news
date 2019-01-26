#!/bin/env python
from datetime import datetime
from newspaper import Article
from langdetect import detect as lang_detect
from common.top_news_config import config
from common.scrape_task_queue import get_scrape_task as get_scrape_task, queue_sleep as queue_sleep
from common.dedupe_task_queue import send_dedupe_task as send_dedupe_task

#SLEEP_TIME = config['newsFetcher']['sleepTime']

def handle_message(task):
    if not isinstance(task, dict):
        print('message is broken')
        return
    try:
        print(task['url'])
        article = Article(task['url'])
        article.download()
        article.parse()
        if not task['author']:
            task['author'] = ', '.join(article.authors)
        if task['publishedAt'] is None:
            task['publishedAt'] = (article.publish_date if article.publish_date else datetime.utcnow()).isoformat(timespec='seconds') + 'Z'
        task['text'] = article.text
        if not task['urlToImage']:
            task['urlToImage'] = article.top_image
        task['language'] = lang_detect(task['description'])
        article.nlp()
        task['keywords'] = article.keywords
        if task['description'] is None:
            task['description'] = article.summary
        send_dedupe_task(task)
    except Exception as e:
        print(e)

def run():
    while True:
        msg = get_scrape_task()
        if msg is None:
            #queue_sleep(SLEEP_TIME)
            break
        else:
            handle_message(msg)

if __name__ == '__main__':
    run()