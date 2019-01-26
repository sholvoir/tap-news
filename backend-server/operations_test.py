from operations import get_news_for_user

def test_get_news_for_user_basic():
    news = get_news_for_user('sholvoir.he@gmail.com', 0)
    assert len(news) > 0
    print('test_get_news_for_user_basic passed')

def test_get_news_for_user_pagination():
    news_page_1 = get_news_for_user('sholvoir.he@gmail.com', 1)
    news_page_2 = get_news_for_user('sholvoir.he@gmail.com', 2)
    digest_page_1_set = set([news['digest'] for news in news_page_1])
    digest_page_2_set = set([news['digest'] for news in news_page_2])
    assert len(digest_page_1_set.intersection(digest_page_2_set)) == 0
    print("test_get_news_for_user_pagination passed!")

if __name__ == "__main__":
    test_get_news_for_user_basic()
    test_get_news_for_user_pagination()
