#!/usr/bin/env python3
'''
    It is the basics of async.
'''

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ It create the tasks """
    task = create_task(wait_random(max_delay))
    return task
