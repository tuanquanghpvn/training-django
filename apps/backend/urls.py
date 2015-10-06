from django.conf.urls import include, url
from apps.backend.views import dashboard, course, subject, task, user_profile

urlpatterns = [
    ######################################
    ######################################
    # Url Dashboard
    url(r'^login', dashboard.doLogin),
    url(r'^logout', dashboard.doLogout),
    url(r'^profile', dashboard.profile), 
    url(r'^$', dashboard.index),

    ######################################
    ######################################
    # Url Subject
    url(r'^subject/$', subject.index),
    url(r'^subject/create', subject.create),
    url(r'^subject/update', subject.update),
    url(r'^subject/delete', subject.delete),
    url(r'^subject/detail', subject.detail),
    url(r'^subject/add-user', subject.add_user_to_subject),
    url(r'^subject/remove-user', subject.remove_user_in_subject),

    ######################################
    ######################################
    # Url Course
    url(r'^course/$', course.index),
    url(r'^course/create', course.create),
    url(r'^course/update', course.update),
    url(r'^course/delete', course.delete),
    url(r'^course/detail', course.detail),
    url(r'^course/add-user', course.add_user_to_course),
    url(r'^course/remove-user', course.remove_user_in_course),
    url(r'^course/remove-subject', course.remove_subject_in_course),

    ######################################
    ######################################
    # Url Task
    url(r'^task/$', task.index),
    url(r'^task/create', task.create),
    url(r'^task/update', task.update),
    url(r'^task/delete', task.delete),
    url(r'^task/detail', task.detail),
    url(r'^task/add-user', task.add_user_to_task),
    url(r'^task/remove-user', task.remove_user_in_task),

    ######################################
    ######################################
    # Url User
    url(r'^user/$', user_profile.index),
    url(r'^user/detail', user_profile.detail),
    url(r'^user/delete', user_profile.delete)
]