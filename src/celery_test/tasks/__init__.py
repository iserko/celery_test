from celery.contrib.batches import Batches

from celery_test import app


@app.task(base=Batches, flush_every=20, flush_interval=10)
def do_something(entries):
    print "Got {} entries".format(len(entries))
    for entry in entries:
        print entry.id, entry.args
