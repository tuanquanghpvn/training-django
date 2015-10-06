from django.shortcuts import render, redirect
from apps.data.models import Course, UserProfileCourse, UserProfile
from apps.data.forms import CourseForm, UserProfileCourseForm
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

#############################################################
#############################################################
# Function view course_index
@permission_required('is_staff', login_url='/admin/login')
def index(request):
    info = {
        'info': {
            'title': 'Manage Course - Admin Training Framgia',
            'sidebar': ['course']
        },
        'data': Course.objects.all()
    }
    return render(request, 'backend/course/course_index.html', info)

#############################################################
#############################################################
# Function view course_create
@permission_required('is_staff', login_url='/admin/login')
def create(request):
    info = {
        'info': {
            'title': 'Create Course - Admin Training Framgia',
            'sidebar': ['course']
        },
        'data': CourseForm(),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.created_at = datetime.now()
            course.update_at = datetime.now()
            course.save()
            info['status']['alert'] = 'info'
            info['status']['message'] = 'Create course success !'
        else:
            info['data'] = course_form
    return render(request, 'backend/course/course_create.html', info)

#############################################################
#############################################################
# Function view udpate course
@permission_required('is_staff', login_url='/admin/login')
def update(request):
    id_course = request.GET.get('id', None)
    if not id_course:
        return redirect('admin/course')
    info = {
        'info': {
            'title': 'Update Course - Admin Training Framgia',
            'sidebar': ['course']
        },
        'data': CourseForm(instance=Course.objects.get(id=id_course)),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=Course.objects.get(id=id_course))
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.update_at = datetime.now()
            course.save()
            info['status']['alert'] = 'info'
            info['status']['message'] = 'Update course success !'
        else:
            info['data'] = course_form
    return render(request, 'backend/course/course_update.html', info)    

#############################################################
#############################################################
# Function delete course
@permission_required('is_staff', login_url='/admin/login')
def delete(request):
    id_course = request.GET.get('id', None)
    if id_course:
        Course.objects.get(id=id_course).delete()
    return redirect('/admin/course')

#############################################################
#############################################################
# Function view detail course: Add user to course, Remove user in course, Remove subject in course
@permission_required('is_staff', login_url='/admin/login')
def detail(request):
    info = {
        'info': {
            'title': 'Detail Course - Admin Training Framgia',
            'sidebar': ['course']
        },
        'data': {}
    }
    id_course = request.GET.get('id', None)
    if id_course:
        info['data']['user_profile_course_form'] = UserProfileCourseForm()
        info['data']['id_course'] = id_course
        info['data']['list_user'] = UserProfile.objects.exclude(user__id__in=Course.objects.get(id=id_course).user_profile.all())
        info['data']['course'] = Course.objects.get(id=id_course)
        info['data']['list_subject'] = Course.objects.get(id=id_course).subject.all()
        info['data']['list_trainee'] = Course.objects.get(id=id_course).user_profile.all()
    return render(request, 'backend/course/course_detail.html', info)

@permission_required('is_staff', login_url='/admin/login')
def add_user_to_course(request):
    if request.method == 'POST':
        id_course = request.POST.get('course', None)
        list_user = request.POST.getlist('user_profile')

        form = UserProfileCourseForm(request.POST)
        if form.is_valid():
            user_profile_course = form.save(commit=False)
            user_profile_course.status = False
            user_profile_course.save()

    url = '/admin/course/detail?id=' + str(id_course)
    return redirect(url)

@permission_required('is_staff', login_url='/admin/login')
def remove_user_in_course(request):
    id_user = request.GET.get('id', None)
    id_course = request.GET.get('idCourse', None)
    # Course.objects.get(id=id_course).user_profile.remove(user__id=id_user)
    UserProfileCourse.objects.get(user_profile__user__id=id_user, course__id=id_course).delete()

    url = '/admin/course/detail?id=' + str(id_course)
    return redirect(url)

@permission_required('is_staff', login_url='/admin/login')
def remove_subject_in_course(request):
    id_subject = request.GET.get('id', None)
    id_course = request.GET.get('idCourse', None)
    Course.objects.get(id=id_course).subject.remove(id_subject)

    url = '/admin/course/detail?id=' + str(id_course)
    return redirect(url)