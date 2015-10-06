from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

##################################################
##################################################
##################################################
# Subject Model

class Subject(models.Model):
    """docstring for Subject"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    begin_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

##################################################
##################################################
##################################################
# Course Model

class Course(models.Model):
    """docstring for Course"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    begin_at = models.DateTimeField()
    end_at = models.DateTimeField()
    subject = models.ManyToManyField(Subject, related_name='course')

    def __str__(self):
        return self.name

##################################################
##################################################
##################################################
# Task Model

class Task(models.Model):
    """docstring for Task"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    begin_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return self.name

##################################################
##################################################
##################################################
# UserProfile Model

class UserProfile(models.Model):
    """docstring for UserProfile"""
    user = models.OneToOneField(User, primary_key=True)
    # Default field in User Django
    # username
    # first_name
    # last_name
    # email
    # password
    # groups
    # user_permissions
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined

    remember = models.BooleanField()
    supervision = models.BooleanField()
    study_status = models.BooleanField()
    update_at = models.DateTimeField(auto_now=True)

    course = models.ManyToManyField(Course, through='UserProfileCourse', related_name='user_profile')
    subject = models.ManyToManyField(Subject, through='UserProfileSubject', related_name='user_profile')
    task = models.ManyToManyField(Task, through='UserProfileTask', related_name='user_profile')    

class UserProfileCourse(models.Model):
    """docstring for UserProfileCourse"""
    id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Course)
    status = models.BooleanField(default=False)

class UserProfileSubject(models.Model):
    """docstring for UserProfileSubject"""
    id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile)
    subject = models.ForeignKey(Subject)
    status = models.BooleanField(default=False)

class UserProfileTask(models.Model):
    """docstring for UserProfileTask"""
    id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile)
    task = models.ForeignKey(Task)
    status = models.BooleanField(default=False)

        
