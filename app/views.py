from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import print_sequence

from celery.result import AsyncResult
from django.http import JsonResponse

def start_task(request):
    task = print_sequence.delay()
    return JsonResponse({'task_id': task.id})

#Check status of task
def task_status(request, task_id):
    task_result = AsyncResult(task_id)

    response = {
        'task_id': task_id,
        'status': task_result.status,
        'result': task_result.result if task_result.status == 'SUCCESS' else None,
    }
    return JsonResponse(response)


def index(request):
    return render(request, 'app/index.html')