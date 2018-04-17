from jsonrpclib import ServerProxy
from .top_news_config import config

_url = 'http://' + config['topicProvideServer']['host'] + ':' + str(config['topicProvideServer']['port'])
_client = ServerProxy(_url)

get_category = _client.get_category