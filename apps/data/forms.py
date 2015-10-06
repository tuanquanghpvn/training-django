from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from apps.data.models import UserProfile, Course, Subject, Task, UserProfileCourse, UserProfileSubject, UserProfileTask

###################################################
###################################################
###################################################
# User Form

class ProfileForm(forms.ModelForm):
    """docstring for ProfileForm"""
    password2 = forms.CharField(label='Re Password')

    class Meta:
        model = User
        fields = ['password']

    def clean(self):
        password1 = self.cleaned_data.get('password', None)
        password2 = self.cleaned_data.get('password2', None)

        if password1 and len(password1) < 6:
            raise ValidationError({'password': ['Lenght password must be larger 6',]})

        if password1 and password1 != password2:
            raise ValidationError({'password2': ['Password and Re Password must be contain!',]})

    def save(self, commit=True):
        user_profile = super(ProfileForm, self).save(commit=False)
        user_profile.set_password(self.cleaned_data["password"])
        if commit:
            user_profile.save()
        return user_profile

class UserForm(forms.ModelForm):
    """docstring for UserForm"""
    class Meta:
        model = User
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    """docstring for UserFrofileForm"""
    class Meta:
        model = UserProfile
        fields = '__all__'

class CourseForm(forms.ModelForm):
    """docstring for CourseForm"""
    class Meta:
        model = Course
        fields = ['name', 'description', 'begin_at', 'end_at']

    def clean(self):
        cleaned_data = super(CourseForm, self).clean()
        begin_at = cleaned_data.get('begin_at', None)
        end_at = cleaned_data.get('end_at', None)

        if end_at and begin_at and end_at < begin_at:
            raise ValidationError({'end_at': ["Date End must be larger Date Begin!",]})

class SubjectForm(forms.ModelForm):
    """docstring for CourseForm"""
    course = forms.ModelMultipleChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Subject
        fields = ['course', 'name', 'description', 'begin_at', 'end_at']

    def clean(self):
        cleaned_data = super(SubjectForm, self).clean()
        begin_at = cleaned_data.get('begin_at', None)
        end_at = cleaned_data.get('end_at', None)

        if end_at and begin_at and end_at < begin_at:
            raise ValidationError({'end_at': ["Date End must be larger Date Begin!",]})

class TaskForm(forms.ModelForm):
    """docstring for CourseForm"""
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_at']

    def clean(self):
        cleaned_data = super(TaskForm, self).clean()
        begin_at = cleaned_data.get('begin_at', None)
        end_at = cleaned_data.get('end_at', None)

        if end_at and begin_at and end_at < begin_at:
            raise ValidationError({'end_at': ["Date End must be larger Date Begin!",]})

class UserProfileCourseForm(forms.ModelForm):
    """docstring for UserFrofileForm"""
    class Meta:
        model = UserProfileCourse
        fields = ['user_profile', 'course']

class UserProfileSubjectForm(forms.ModelForm):
    """docstring for UserFrofileForm"""
    class Meta:
        model = UserProfileSubject
        fields = ['user_profile', 'subject']

class UserProfileTaskForm(forms.ModelForm):
    """docstring for UserFrofileForm"""
    class Meta:
        model = UserProfileTask
        fields = ['user_profile', 'task']
