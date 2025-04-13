from django.shortcuts import render

def task_list_view(request):
    return render(request, 'tasks/task_list.html')

def create_task_view(request):
    return render(request, 'tasks/create_task.html')