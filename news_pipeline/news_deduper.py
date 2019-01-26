#!/bin/env python
from datetime import datetime, timedelta
from sklearn.feature_extraction.text import TfidfVectorizer
from common.top_news_config import config
from common.dedupe_task_queue import get_dedupe_task as get_dedupe_task, queue_sleep as queue_sleep
from common.mongodb_news import news_table

DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
#SLEEP_TIME = config['newsDeduper']['sleepTime']
SAME_NEWS_SIMILARITY_THRESHOLD = config['newsDeduper']['sameNewsSimilarityThreshold']

def handle_task(task):
    if not isinstance(task, dict):
        return
    text = task['text']
    if text is None:
        return
    try:
        print(task['url'])
        publish_time = datetime.strptime(task['publishedAt'], DATE_FORMAT)
        timespan = timedelta(hours=12)
        publish_begin_time = publish_time - timespan
        publish_end_time = publish_time + timespan
        span_time_news_list = list(news_table.find({
            'publishedAt': {
                '$gte': publish_begin_time,
                '$lt': publish_end_time
            }
        }))
        if span_time_news_list is not None and len(span_time_news_list) > 0:
            documents = [news['text'] for news in span_time_news_list]
            documents.insert(0, text)
            tfidf = TfidfVectorizer().fit_transform(documents)
            pairwise_sim = tfidf * tfidf.T
            rows, _ = pairwise_sim.shape
            for row in range(1, rows):
                if pairwise_sim[row, 0] > SAME_NEWS_SIMILARITY_THRESHOLD:
                    return
        task['publishedAt'] = publish_time
        news_table.replace_one({'digest': task['digest']}, task, upsert=True)
    except Exception as e:
        print(e)

def run():
    while True:
        task = get_dedupe_task()
        if task is None:
            #queue_sleep(SLEEP_TIME)
            break
        else:
            handle_task(task)
            
if __name__ == '__main__':
    run()
