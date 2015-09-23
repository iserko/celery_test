import argparse
import random

from celery_test import tasks


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('task_name', help='Name of the task to send the items to')
    parser.add_argument('number', help='How many items to put to the queue', type=int)
    args = parser.parse_args()
    func = getattr(tasks, args.task_name)
    if not func:
        args.error('Task %s does not exist' % args.task_name)
    for entry in range(args.number):
        func.delay('cookies-{}-{}'.format(entry, random.randint(100, 1000)))


if __name__ == '__main__':
    run()
