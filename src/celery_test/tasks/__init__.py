from celery.contrib.batches import Batches

from celery_test import app


@app.task(base=Batches, flush_every=30, flush_interval=10, max_retries=5)
def batch_exceptions(requests):
    print "Got {} requests".format(len(requests))
    for request in requests:
        print request.id, request.args
        raise Exception("BOOM")
