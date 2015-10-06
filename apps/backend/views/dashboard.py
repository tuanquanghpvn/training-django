from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from apps.data.forms import ProfileForm

def doLogin(request):
    info = {
        'status': True,
        'message': ''
    }
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/admin')
            else:
                # Return a 'disabled account' error message
                info = {
                    'status': False,
                    'message': 'Account is disabled !'
                }
        else:
            info = {
                'status': False,
                'message': 'Login fail !'
            }
    return render(request, 'backend/layout/login.html', { 'info': info })

def doLogout(request):
    logout(request)
    return redirect('/admin/login')

@permission_required('is_staff', login_url='/admin/login')
def index(request):
    info = {
        'info': {
            'title': 'Dashboard - Admin Training Framgia',
            'sidebar': ['dashboard']
        }
    }
    return render(request, 'backend/dashboard/dashboard_index.html', info)

@permission_required('is_staff', login_url='/admin/login')
def profile(request):
    info = {
        'info': {
            'title': 'Change Profile - Admin Training Framgia',
            'sidebar': []
        },
        'data': ProfileForm(),
        'status': {
            'alert': '',
            'message': ''
        }
    }
    if request.method == 'POST':
        # new_password = request.POST.get('password', None)
        # if new_password:
        profile_form = ProfileForm(request.POST, instance=User.objects.get(id=request.user.id))
        if profile_form.is_valid():
            changed = profile_form.save()
            if changed:

                username = request.user.username
                new_password = request.POST.get('password', None)

                logout(request)
                # Re login
                user = authenticate(username=username, password=new_password)
                if user is not None:
                    if user.is_active:
                        login(request, user)

            info['status']['alert'] = 'info'
            info['status']['message'] = 'Change password profile success!'
        else:
            info['data'] = profile_form

    return render(request, 'backend/dashboard/dashboard_profile.html', info)

