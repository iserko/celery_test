batch-exception-worker:
	docker-compose run -e CELERYD_PREFETCH_MULTIPLIER=60 celery \
		celery -A celery_test -Q celery.batch_exceptions worker
batch-exception-populate:
	docker-compose run celery python -m celery_test.populate batch_exceptions 1000
