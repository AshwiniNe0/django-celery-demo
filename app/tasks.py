from __future__ import absolute_import, unicode_literals

# app/tasks.py
from celery import shared_task
import time

@shared_task
def print_sequence():
    sequence = []
    for i in range(1, 11):
        sequence.append(i)
        print(i)
        time.sleep(1)  # Simulate a long-running task
    return sequence
