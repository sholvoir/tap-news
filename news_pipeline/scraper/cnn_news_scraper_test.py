#!/bin/env python
import cnn_news_scraper as scraper

EXPECTED_NEWS = "Tillis and Graham also joined with Grassley last week to call for a second special counsel to investigate alleged abuses by the FBI and the Justice Department's handling of the Trump-Russia investigation up until the appointment of Mueller — a move that backs up complaints made by Trump about the Justice Department."

CNN_NEWS_URL = 'https://www.cnn.com/2018/03/18/politics/mueller-trump-congress/index.html'

def test_basic():
    news = scraper.extract_news(CNN_NEWS_URL)
    print(news)
    assert EXPECTED_NEWS in news
    print('test_basic passed!')

if __name__ == '__main__':
    test_basic()
    