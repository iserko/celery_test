import argparse
import random

from celery_test.tasks import do_something


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='How many items to put to the queue', type=int, default=1)
    args = parser.parse_args()
    for entry in range(args.number):
        do_something.delay('cookies-{}-{}'.format(entry, random.randint(100, 1000)))


if __name__ == '__main__':
    run()
