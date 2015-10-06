# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('begin_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('begin_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('begin_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('subject', models.ForeignKey(to='data.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('remember', models.BooleanField()),
                ('supervision', models.BooleanField()),
                ('study_status', models.BooleanField()),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='data.Course')),
                ('user_profile', models.ForeignKey(to='data.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileSubject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(to='data.Subject')),
                ('user_profile', models.ForeignKey(to='data.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('task', models.ForeignKey(to='data.Task')),
                ('user_profile', models.ForeignKey(to='data.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.ManyToManyField(through='data.UserProfileCourse', related_name='user_profile', to='data.Course'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subject',
            field=models.ManyToManyField(through='data.UserProfileSubject', related_name='user_profile', to='data.Subject'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='task',
            field=models.ManyToManyField(through='data.UserProfileTask', related_name='user_profile', to='data.Task'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(related_name='course', to='data.Subject'),
        ),
    ]
