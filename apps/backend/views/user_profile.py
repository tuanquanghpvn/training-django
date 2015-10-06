from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.data.models import Subject, UserProfile, UserProfileTask, UserProfileSubject, UserProfileCourse
from apps.data.forms import UserProfileForm
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@permission_required('is_staff', login_url='/admin/login')
def index(request):
    info = {
        'info': {
            'title': 'Manage UserProfile - Admin Training Framgia',
            'sidebar': ['user']
        },
        'data': UserProfile.objects.all()
    }
    return render(request, 'backend/user_profile/user_profile_index.html', info)

@permission_required('is_staff', login_url='/admin/login')
def detail(request):
    id_user = request.GET.get('id', None)
    if not id_user:
        return redirect('admin/user')
    info = {
        'info': {
            'title': 'Detail UserProfile - Admin Training Framgia',
            'sidebar': ['user']
        },
        'data': {
            'user_profile': UserProfile.objects.get(user__id=id_user),
            'list_task': UserProfileTask.objects.filter(user_profile__user__id=id_user),
            'list_subject': UserProfileSubject.objects.filter(user_profile__user__id=id_user),
            'list_course': UserProfileCourse.objects.filter(user_profile__user__id=id_user)
        }
    }
    return render(request, 'backend/user_profile/user_profile_detail.html', info)    

@permission_required('is_staff', login_url='/admin/login')
def delete(request):
    id_user = request.GET.get('id', None)
    if id_user:        
        # Delete UserProfile before delete User
        UserProfile.objects.get(user__id=id_user).delete()
        User.objects.get(id=id_user).delete()
    return redirect('/admin/user')
