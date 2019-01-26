#!/usr/bin/env python
from common.cloudAMQP_client import CloudAMQPClient
from common.top_news_config import config

TEST_QUEUE_NAME = "test"

def test_basic(queue_url, queue_name):
    client = CloudAMQPClient(queue_url, queue_name)
    sentMsg = {'test': 'test'}
    client.send_message(sentMsg)
    receiveMsg = client.get_message()
    assert sentMsg == receiveMsg
    print('test_basic passed.')

if __name__ == "__main__":
    test_basic(config['scrapeTaskQueue']['url'], TEST_QUEUE_NAME)
    test_basic(config['dedupeTaskQueue']['url'], TEST_QUEUE_NAME)