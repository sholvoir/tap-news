#!/usr/bin/env python
"""Backend Service"""
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from common.top_news_config import config
from operations import more_news_for_user, clear_news_for_user, log_news_click_for_user

backend_server_cfg = (config['backendServer']['host'], config['backendServer']['port'])
server = SimpleJSONRPCServer(backend_server_cfg)

server.register_function(more_news_for_user, 'moreNewsForUser')
server.register_function(clear_news_for_user, 'clearNewsForUser')
server.register_function(log_news_click_for_user, 'logNewsClickForUser')
print("Starting RPC server on %s:%d" % backend_server_cfg)
server.serve_forever()
