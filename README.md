# celery_test

I've been frustrated about not knowing how Celery's Batches
http://celery.readthedocs.org/en/latest/reference/celery.contrib.batches.html work, so I made
this test in order to see what problems can occur.


## Warning

Make sure you never use `--without-hearbeat` or `--without-gossip` when running a worker, as it will
make batch workers never process anything.


## Lost messages


Wrote a task to test exception handling in Batches:
https://github.com/iserko/celery_test/blob/master/src/celery_test/tasks/__init__.py#L6

### Conclusion:
If an exception happens in the middle of the batch, one exception message is logged, and the other
messages in the batch are just thrown away.
ACKS_LATE setting has no effect on this.

### Test if for yourself:

Start the worker: `make batch-exception-worker`

Populate the queue: `make batch-exception-populate`

### Results:

```
[2015-09-23 10:04:26,398: WARNING/Worker-1] Got 30 requests
[2015-09-23 10:04:26,399: WARNING/Worker-1] 176d9f28-0148-4851-86d2-9e13368b13a3
[2015-09-23 10:04:26,400: WARNING/Worker-1] ('cookies-930-896',)
[2015-09-23 10:04:26,401: ERROR/Worker-1] Error: Exception('BOOM',)
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/celery/contrib/batches.py", line 126, in apply_batches_task
    result = task(*args)
  File "/usr/local/lib/python2.7/site-packages/celery/app/trace.py", line 439, in __protected_call__
    return orig(self, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/celery/app/task.py", line 420, in __call__
    return self.run(*args, **kwargs)
  File "/home/code/src/celery_test/tasks/__init__.py", line 11, in batch_exceptions
    raise Exception("BOOM")
Exception: BOOM
[2015-09-23 10:04:26,454: WARNING/Worker-1] Got 30 requests
[2015-09-23 10:04:26,455: WARNING/Worker-1] 4e43f294-0037-4368-aece-6938a1404a41
[2015-09-23 10:04:26,456: WARNING/Worker-1] ('cookies-960-315',)
[2015-09-23 10:04:26,457: ERROR/Worker-1] Error: Exception('BOOM',)
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/celery/contrib/batches.py", line 126, in apply_batches_task
    result = task(*args)
  File "/usr/local/lib/python2.7/site-packages/celery/app/trace.py", line 439, in __protected_call__
    return orig(self, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/celery/app/task.py", line 420, in __call__
    return self.run(*args, **kwargs)
  File "/home/code/src/celery_test/tasks/__init__.py", line 11, in batch_exceptions
    raise Exception("BOOM")
Exception: BOOM
```
