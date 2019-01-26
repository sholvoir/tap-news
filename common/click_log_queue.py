#!/bin/env python
from pika import URLParameters, BlockingConnection
from json import loads as json_loads, dumps as json_dumps
from .top_news_config import config

queue_cfg = config['clickLogQueue']

queue_name = queue_cfg['name']
params = URLParameters(queue_cfg['url'])
params.socket_timeout = 3
connection = None
channel = None

def queue_reset():
    global connection, channel
    connection = BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

def queue_sleep(seconds):
    if connection.is_open:
        connection.sleep(seconds)

def send_click_log(task):
    body = json_dumps(task)
    try:
        channel.basic_publish(exchange='', routing_key=queue_name, body=body)
    except Exception:
        queue_reset()
        channel.basic_publish(exchange='', routing_key=queue_name, body=body)

def get_click_log():
    method = None
    body = None
    try:
        method, _, body = channel.basic_get(queue_name)
    except Exception:
        queue_reset()
        method, _, body = channel.basic_get(queue_name)
    
    if method and body:
        channel.basic_ack(method.delivery_tag)
        return json_loads(body.decode())
    else:
        print("No message returned")
        return None

queue_reset()
