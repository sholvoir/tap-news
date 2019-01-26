#!/bin/env python
import os
import random
import requests

from lxml import html

GET_CNN_NEWS_XPATH = "//p[contains(@class, 'zn-body__paragraph')]//text() | //div[contains(@class, 'zn-body__paragraph')]//text()"

USER_AGENTS_FILE = os.path.join(os.path.dirname(__file__), 'user_agents.txt')
USER_AGENTS = []

with open(USER_AGENTS_FILE, 'r') as uaf:
    for ua in uaf.readlines():
        ua = ua.strip()
        if ua:
            USER_AGENTS.append(ua)

def _get_header():
    return {
        "User-Agent": random.choice(USER_AGENTS)
    }

def extract_news(news_url):
    session_requests = requests.session()
    response = session_requests.get(news_url, headers=_get_header())

    try:
        return '. '.join(html.fromstring(response.content).xpath(GET_CNN_NEWS_XPATH))
    except Exception:
        return ''