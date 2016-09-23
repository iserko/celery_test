import time

from celery.contrib.batches import Batches

from celery_test import app


# 30 tasks or 10 seconds
@app.task(base=Batches, flush_every=30, flush_interval=10)
def batch_exceptions(requests):
    print "Got {} requests".format(len(requests))
    for request in requests:
        print request.id, request.args
        raise Exception("BOOM")


# 30 tasks or 10 seconds ... 5 retries
@app.task(base=Batches, flush_every=30, flush_interval=10, max_retries=5)
def batch_exceptions_retries(requests):
    print "Got {} requests".format(len(requests))
    for request in requests:
        print request.id, request.args
        raise Exception("BOOM")


# 30 tasks or 60 seconds
@app.task(base=Batches, flush_every=30, flush_interval=60)
def batch_timeout(requests):
    print "Got {} requests".format(len(requests))
    for request in requests:
        print request.id, request.args
        print "Sleeping for 65 seconds"
        time.sleep(65)
