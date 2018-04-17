#!/bin/env python
from common.mongodb_news import client

def test_basic():
    db = client['test']
    db.test.drop()
    assert db.test.count() == 0
    db.test.insert({'test': 1})
    assert db.test.count() == 1
    db.test.drop()
    print('test_basic passed.')

if __name__ == '__main__':
    test_basic()