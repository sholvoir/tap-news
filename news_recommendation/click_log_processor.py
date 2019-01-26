#!/bin/env python
"""
Time decay model:
If selected:
p = (1-α)p + α
If not:
p = (1-α)p
Where p is the selection probability, and α is the degree of weight decrease.
The result of this is that the nth most recent selection will have a weight of
(1-α)^n. Using a coefficient value of 0.05 as an example, the 10th most recent
selection would only have half the weight of the most recent. Increasing
epsilon
would bias towards more recent results more.
"""
from common.mongodb_preference import preference_table
from common.mongodb_news import news_table
from common.click_log_queue import get_click_log
from common.top_news_config import config

click_log_processor_cfg = config["clickLogProcessor"]
CATEGORY_ALPHA = click_log_processor_cfg["categoryAlpha"]
COUNTRY_ALPHA = click_log_processor_cfg["countryAlpha"]
LANGUAGE_ALPHA = click_log_processor_cfg["languageAlpha"]

news_api_cfg = config['newsAPI']
categories = news_api_cfg['categories']
countries = news_api_cfg['countries']
languages = news_api_cfg['languages']

def handle_click_log(msg):
    if not isinstance(msg, dict):
        return
    if ('userId' not in msg
        or 'newsDigest' not in msg):
        return
    user_id = msg['userId']
    news_digest = msg['newsDigest']

    preference = preference_table.find_one({'userId': user_id})
    if preference is None:
        init_category_p = 1.0 / len(categories)
        init_country_p = 1.0 / len(countries)
        inti_language_p = 1.0 / len(languages)
        print('Creat preference for new user: %s' % user_id)
        preference = {'userId': user_id}
        preference_category = {}
        for category in categories:
            preference_category[category] = init_category_p
        preference_country = {}
        for country in countries:
            preference_country[country] = init_country_p
        preference_language = {}
        for language in languages:
            preference_language[language] = inti_language_p
        preference['category'] = preference_category
        preference['country'] = preference_country
        preference['language'] = preference_language
        preference['keywords'] = {}
    
    print('Update preference for user: %s' % user_id)
    news = news_table.find_one({'digest': news_digest})
    if (news is None):
        print("Not found news, skip...")
        return
    if 'category' in news:
        click_category = news['category']
        if click_category in categories:
            preference_category = preference['category']
            for category, prob in preference_category.items():
                preference_category[category] = (1 - CATEGORY_ALPHA) * prob + CATEGORY_ALPHA \
                    if category == click_category else (1 - CATEGORY_ALPHA) * prob
    if 'country' in news:
        click_country = news['country']
        if click_country in countries:
            preference_country = preference['country']
            for country, prob in preference_country.items():
                preference_country[country] = (1 - COUNTRY_ALPHA) * prob + CATEGORY_ALPHA \
                    if country == click_country else (1 - COUNTRY_ALPHA) * prob
    if 'language' in news:
        click_language = news['language']
        if click_language in languages:
            preference_language = preference['language']
            for language, prob in preference_language.items():
                preference_language[language] = (1 - LANGUAGE_ALPHA) * prob + LANGUAGE_ALPHA \
                    if language == click_language else (1 - LANGUAGE_ALPHA) * prob
    if 'keywords' in news:
        click_keywords = news['keywords']
        if click_keywords is not None:
            preference_keywords = preference['keywords']
            for click_keyword in click_keywords:
                old_prob = preference_keywords[click_keyword]
                preference_keywords[click_keyword] = old_prob + 1 \
                    if old_prob is not None else 1
    
    preference_table.replace_one({'userId': user_id}, preference, upsert=True)


def run():
    while True:
        msg = get_click_log()
        if msg is None:
            break
        try:
            handle_click_log(msg)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    run()