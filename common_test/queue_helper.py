from common.cloudAMQP_client import CloudAMQPClient
from common.top_news_config import config

def clear_queue(queue_url, queue_name):
    client = CloudAMQPClient(queue_url, queue_name)
    messages_num = 0
    if client is not None:
        while True:
            msg = client.get_message()
            if msg is not None:
                messages_num += 1
            else:
                print('Cleared %d messages.' % messages_num)
                break
            

if __name__ == '__main__':
    clear_queue(config['scrapeTaskQueue']['url'], config['scrapeTaskQueue']['name'])
    clear_queue(config['dedupeTaskQueue']['url'], config['dedupeTaskQueue']['name'])