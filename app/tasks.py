from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time

@shared_task
def print_sequence1():
    sequence = []
    for i in range(1, 11):
        sequence.append(i)
        print(i)
        time.sleep(1)  # Simulate a long-running task
    return sequence

@shared_task
def print_sequence2():
    sequence = []
    for i in range(11, 21):
        sequence.append(i)
        print(i)
        time.sleep(1)  # Simulate a long-running task
    return sequence

@shared_task
def print_sequence3():
    sequence = []
    for i in range(21, 31):
        sequence.append(i)
        print(i)
        time.sleep(1)  # Simulate a long-running task
    return sequence