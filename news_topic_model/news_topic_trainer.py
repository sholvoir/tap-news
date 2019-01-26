import os
import pickle
import shutil
import tensorflow as tf
import numpy as np
import random
from sklearn import metrics
from common.top_news_config import news_topic_model_cfg, news_api_cfg
from common.mongodb_news import news_table
from common.news_summary import get_summary
from news_cnn_model import generate_cnn_model

REMOVE_PREVIOUS_MODEL = True
current_path = os.path.dirname(__file__)
MODEL_OUTPUT_DIR = os.path.join(current_path, *news_topic_model_cfg["modelPath"])
VARS_FILE =  os.path.join(current_path, *news_topic_model_cfg["varsFile"])
VOCABULARY_FILE = os.path.join(current_path, *news_topic_model_cfg["vocabularyFile"])
MAX_DOCUMENT_LENGTH = news_topic_model_cfg['maxDocumentLength']
TRAIN_STEPS = news_topic_model_cfg['trainSteps']

categories = news_api_cfg['categories']
category_dict = dict((val, i) for i, val in enumerate(categories))
N_CATEGORIES = len(categories)

learn = tf.contrib.learn

def main(argv):
    if REMOVE_PREVIOUS_MODEL:
        print('Removing previous model...')
        shutil.rmtree(MODEL_OUTPUT_DIR)
        os.mkdir(MODEL_OUTPUT_DIR)

    df = list(news_table.aggregate([{"$match": {'language': 'en'}}, {'$sample': {'size': 1000}}]))
    random.shuffle(df)
    train_df = df[0:800]
    test_df = df[800:]

    x_train = [get_summary(x) for x in train_df]
    y_train = [category_dict[x['category']] for x in train_df]
    x_test = [get_summary(x) for x in test_df]
    y_test = [category_dict[x['category']] for x in test_df]

    vocabulary_processor = learn.preprocessing.VocabularyProcessor(MAX_DOCUMENT_LENGTH)
    x_train = np.array(list(vocabulary_processor.fit_transform(x_train)))
    x_test = np.array(list(vocabulary_processor.transform(x_test)))

    n_words = len(vocabulary_processor.vocabulary_)
    print('Total words: %d' % n_words)

    with open(VARS_FILE, 'wb') as f:
        pickle.dump(n_words, f)

    vocabulary_processor.save(VOCABULARY_FILE)

    classifier = learn.Estimator(
        model_fn=generate_cnn_model(N_CATEGORIES, n_words),
        model_dir=MODEL_OUTPUT_DIR)

    classifier.fit(x_train, y_train, steps=TRAIN_STEPS)

    y_predicted = [p['category'] for p in classifier.predict(x_test, as_iterable=True)]
    score = metrics.accuracy_score(y_test, y_predicted)
    print('Accuracy: {0:f}'.format(score))

if __name__ == '__main__':
    tf.app.run(main=main)