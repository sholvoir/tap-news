from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from common.mongodb_preference import preference_table
from common.top_news_config import config

recommendation_server_cfg = (config['recommendationServer']['host'], config['recommendationServer']['port'])
server = SimpleJSONRPCServer(recommendation_server_cfg)

def get_preference_for_user(user_id):
    preference = preference_table.find_one({"userId": user_id})
    del preference['_id']
    return preference

server.register_function(get_preference_for_user, 'getPreferenceForUser')
print("Starting RPC server on %s:%d" % recommendation_server_cfg)
server.serve_forever()