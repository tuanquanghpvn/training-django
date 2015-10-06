from django.shortcuts import render, redirect
from apps.data.models import Course, Subject, UserProfile, UserProfileSubject, UserProfileCourse
from apps.data.forms import SubjectForm, UserProfileSubjectForm
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@permission_required('is_staff', login_url='/admin/login')
def index(request):
    info = {
        'info': {
            'title': 'Manage Subject - Admin Training Framgia',
            'sidebar': ['subject']
        },
        'data': Subject.objects.all()
    }
    return render(request, 'backend/subject/subject_index.html', info)

@permission_required('is_staff', login_url='/admin/login')
def create(request):
    info = {
        'info': {
            'title': 'Create Subject - Admin Training Framgia',
            'sidebar': ['subject']
        },
        'data': SubjectForm(),
        'list_course': Course.objects.all(),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        subject_form = SubjectForm(data=request.POST)
        if subject_form.is_valid():            
            subject = subject_form.save(commit=False)
            subject.created_at = datetime.now()
            subject.update_at = datetime.now()
            subject.save()
            subject.course = subject_form.cleaned_data['course']
            subject.save()
            
            info['status']['alert'] = 'info'
            info['status']['message'] = 'Create subject success !'
        else:
            info['data'] = subject_form
            info['list_course_selected'] = list(map(int, request.POST.getlist('course')))

    return render(request, 'backend/subject/subject_create.html', info)

@permission_required('is_staff', login_url='/admin/login')
def update(request):
    id_subject = request.GET.get('id', None)
    if not id_subject:
        return redirect('admin/subject')
    info = {
        'info': {
            'title': 'Update Subject - Admin Training Framgia',
            'sidebar': ['subject']
        },
        'data': SubjectForm(instance=Subject.objects.get(id=id_subject)),
        'list_course': Course.objects.all(),
        'list_course_selected': Subject.objects.get(id=id_subject).course.all().values_list('id', flat=True),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST, instance=Subject.objects.get(id=id_subject))
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)
            subject.update_at = datetime.now()
            subject.course = subject_form.cleaned_data['course']
            subject.save()

            info['status']['alert'] = 'info'
            info['status']['message'] = 'Update subject success !'
        else:
            info['data'] = subject_form
    return render(request, 'backend/subject/subject_update.html', info)    

@permission_required('is_staff', login_url='/admin/login')
def delete(request):
    id_subject = request.GET.get('id', None)
    if id_subject:
        Subject.objects.get(id=id_subject).delete()
    return redirect('/admin/subject')

@permission_required('is_staff', login_url='/admin/login')
def detail(request):
    info = {
        'info': {
            'title': 'Detail Subject - Admin Training Framgia',
            'sidebar': ['subject']
        },
        'data': {}
    }
    id_subject = request.GET.get('id', None)
    if id_subject:
        info['data']['user_profile_subject_form'] = UserProfileSubjectForm()
        info['data']['id_subject'] = id_subject
        info['data']['list_user'] = UserProfileCourse.objects.exclude(user_profile__user__id__in=Subject.objects.get(id=id_subject).user_profile.all())
        info['data']['subject'] = Subject.objects.get(id=id_subject)
        info['data']['list_trainee'] = Subject.objects.get(id=id_subject).user_profile.all()
    return render(request, 'backend/subject/subject_detail.html', info)

@permission_required('is_staff', login_url='/admin/login')
def add_user_to_subject(request):
    if request.method == 'POST':
        id_subject = request.POST.get('subject', None)
        list_user = request.POST.getlist('user_profile')

        form = UserProfileSubjectForm(request.POST)
        if form.is_valid():
            user_profile_subject = form.save(commit=False)
            user_profile_subject.status = False
            user_profile_subject.save()

    url = '/admin/subject/detail?id=' + str(id_subject)
    return redirect(url)

@permission_required('is_staff', login_url='/admin/login')
def remove_user_in_subject(request):
    id_user = request.GET.get('id', None)
    id_subject = request.GET.get('idSubject', None)
    UserProfileSubject.objects.get(user_profile__user__id=id_user, subject__id=id_subject).delete()

    url = '/admin/subject/detail?id=' + str(id_subject)
    return redirect(url)
