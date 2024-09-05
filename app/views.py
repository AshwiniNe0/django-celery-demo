from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import print_sequence1, print_sequence2, print_sequence3

from celery.result import AsyncResult
from django.http import JsonResponse

def start_task(request):
    task_ids = []
    
    # Existing task
    task_1 = print_sequence1.delay()
    task_ids.append(task_1.id)
    
    # New tasks
    task_2 = print_sequence2.delay()
    task_ids.append(task_2.id)
    task_3 = print_sequence3.delay()
    task_ids.append(task_3.id)

    return JsonResponse({'task_ids': task_ids})


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