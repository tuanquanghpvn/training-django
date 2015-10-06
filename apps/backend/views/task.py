from django.shortcuts import render, redirect
from apps.data.models import Subject, Task, UserProfileTask, UserProfileSubject
from apps.data.forms import TaskForm, UserProfileTaskForm
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@permission_required('is_staff', login_url='/admin/login')
def index(request):
    info = {
        'info': {
            'title': 'Manage Task - Admin Training Framgia',
            'sidebar': ['task']
        },
        'data': Task.objects.all()
    }
    return render(request, 'backend/task/task_index.html', info)

@permission_required('is_staff', login_url='/admin/login')
def create(request):
    info = {
        'info': {
            'title': 'Create Task - Admin Training Framgia',
            'sidebar': ['task']
        },
        'data': TaskForm(),
        'list_subject': Subject.objects.all(),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.created_at = datetime.now()
            task.save()
            info['status']['alert'] = 'info'
            info['status']['message'] = 'Create task success !'
        else:
            info['data'] = task_form
    return render(request, 'backend/task/task_create.html', info)

@permission_required('is_staff', login_url='/admin/login')
def update(request):
    id_task = request.GET.get('id', None)
    if not id_task:
        return redirect('admin/task')
    info = {
        'info': {
            'title': 'Update Task - Admin Training Framgia',
            'sidebar': ['task']
        },
        'list_subject': Subject.objects.all(),
        'data': TaskForm(instance=Task.objects.get(id=id_task)),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=Task.objects.get(id=id_task))
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.save()
            info['status']['alert'] = 'info'
            info['status']['message'] = 'Update task success !'
        else:
            info['data'] = task_form
    return render(request, 'backend/task/task_update.html', info)    

@permission_required('is_staff', login_url='/admin/login')
def delete(request):
    id_task = request.GET.get('id', None)
    if id_task:
        Task.objects.get(id=id_task).delete()
    return redirect('/admin/task')


@permission_required('is_staff', login_url='/admin/login')
def detail(request):
    info = {
        'info': {
            'title': 'Detail Task - Admin Training Framgia',
            'sidebar': ['task']
        },
        'data': {}
    }
    id_task = request.GET.get('id', None)
    if id_task:
        info['data']['user_profile_task_form'] = UserProfileTaskForm()
        info['data']['id_task'] = id_task
        info['data']['list_user'] = UserProfileSubject.objects.exclude(user_profile__user__id__in=Task.objects.get(id=id_task).user_profile.all())
        info['data']['task'] = Task.objects.get(id=id_task)
        info['data']['list_trainee'] = Task.objects.get(id=id_task).user_profile.all()
    return render(request, 'backend/task/task_detail.html', info)

@permission_required('is_staff', login_url='/admin/login')
def add_user_to_task(request):
    if request.method == 'POST':
        id_task = request.POST.get('task', None)
        list_user = request.POST.getlist('user_profile')

        form = UserProfileTaskForm(request.POST)
        if form.is_valid():
            user_profile_task = form.save(commit=False)
            user_profile_task.status = False
            user_profile_task.save()

    url = '/admin/task/detail?id=' + str(id_task)
    return redirect(url)

@permission_required('is_staff', login_url='/admin/login')
def remove_user_in_task(request):
    id_user = request.GET.get('id', None)
    id_task = request.GET.get('idTask', None)
    UserProfileTask.objects.get(user_profile__user__id=id_user, task__id=id_task).delete()

    url = '/admin/task/detail?id=' + str(id_task)
    return redirect(url)