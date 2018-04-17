from redis import StrictRedis
from .top_news_config import config

_redis_cfg = config['userNewsCacheRedis']
redis_client = StrictRedis(_redis_cfg['host'], _redis_cfg['port'])