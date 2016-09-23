batch-exception-worker:
	docker-compose run -e CELERYD_PREFETCH_MULTIPLIER=60 celery \
		celery -A celery_test -Q celery.batch_exceptions worker
batch-exception-populate:
	docker-compose run celery python -m celery_test.populate batch_exceptions 1000

batch-exception-retries-worker:
	docker-compose run -e CELERYD_PREFETCH_MULTIPLIER=60 celery \
		celery -A celery_test -Q celery.batch_exceptions_retries worker

batch-exception-retries-populate:
	docker-compose run celery python -m celery_test.populate batch_exceptions_retries 1000

batch-timeout-worker:
	docker-compose run -e CELERYD_TASK_SOFT_TIME_LIMIT=10 -e CELERYD_PREFETCH_MULTIPLIER=60 celery \
		celery -A celery_test -Q celery.batch_timeout worker

batch-timeout-populate:
	docker-compose run celery python -m celery_test.populate batch_timeout 1000
