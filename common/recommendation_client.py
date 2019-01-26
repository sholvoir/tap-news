from jsonrpclib import ServerProxy
from .top_news_config import config

url = 'http://' + config["recommendationServer"]["host"] + ":" + str(config["recommendationServer"]["port"]) + '/'
server = ServerProxy(url)
getPreferenceForUser = server.getPreferenceForUser
