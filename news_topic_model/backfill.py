from common.mongodb_news import news_table
from common.topic_provider_client import get_category
from common.news_summary import get_summary

def run():
    count = categorify = 0
    cursor = news_table.find({})
    for news in cursor:
        count += 1
        if 'category' not in news:
            text = get_summary(news)
            news['category'] = get_category(text)
            news_table.replace_one({'digest': news['digest']}, news, upsert=True)
            categorify += 1
    print('Total: %d. Categorify: %d' % (count, categorify))

if __name__ == '__main__':
    run()