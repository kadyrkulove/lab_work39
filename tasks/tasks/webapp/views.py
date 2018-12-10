from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    return render(request, 'index.html', context={
        'tasks': Task.objects.all()
    })


def create_task_view(request):
    task = Task.objects.create(
        title=request.POST.get('task_name')
    )
    return redirect('task_index')


def delete_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('task_index')

def edit_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'edit.html', context={
            'task': task
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
        # print(request.POST, '=====1')
        #
        # status = request.POST.get('status')
        # if status:
        #     task.status = status
        #
        # description = request.POST.get('description')
        # if description:
        #     task.description = description
        #
        # task.description = request.POST.get('description')
        # task.status = request.POST.get('status') #TODO
        task.save()

        return redirect('task_index')