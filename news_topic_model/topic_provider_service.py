import numpy as np
import pickle
import tensorflow as tf
import time
import pandas as pd

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
#from tensorflow.contrib.learn.python.learn.estimators import model_fn
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from common.top_news_config import config
from news_cnn_model import generate_cnn_model

categories = config['newsAPI']['categories']
server_cfg = (config['topicProvideServer']['host'], config['topicProvideServer']['port'])

learn = tf.contrib.learn


MODEL_DIR = '../model'
MODEL_UPDATE_LAG_IN_SECONDS = 10
N_CLASSES = 8
VARS_FILE = '../model/vars'
VOCAB_PROCESSOR_SAVE_FILE = '../model/vocab_procesor_save_file'
n_words = 0
MAX_DOCUMENT_LENGTH = 500
vocab_processor = None
classifier = None

def restoreVars():
    global n_words, vocab_processor
    with open(VARS_FILE, 'rb') as f:
        n_words = pickle.load(f)
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(VOCAB_PROCESSOR_SAVE_FILE)

def loadModel():
    global classifier
    classifier = learn.Estimator(
        model_fn=generate_cnn_model(N_CLASSES, n_words),
        model_dir=MODEL_DIR
    )

restoreVars()
loadModel()
print("model Loader")

class ReloadModelHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print("Model update detected. Loading new model")
        time.sleep(MODEL_UPDATE_LAG_IN_SECONDS)
        restoreVars()
        loadModel()

observer = Observer()
observer.schedule(ReloadModelHandler(), path=MODEL_DIR, recursive=False)
observer.start()

def get_category(text):
    text_series = pd.Series([text])
    predict_x = np.array(list(vocab_processor.transform(text_series)))
    print(predict_x)
    y_predicted = [p['category'] for p in classifier.predict(predict_x, as_iterable=True)]
    print(y_predicted[0])
    topic = categories[y_predicted[0]]
    return topic

server = SimpleJSONRPCServer(server_cfg)
server.register_function(get_category, 'getCategory')
print('String Topic Provider Server on %s:%d' % server_cfg)
server.serve_forever()