# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-18 09:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric and have how minimum six characters', regex='^[a-zA-Z0-9-]{6,}$')])),
                ('email', models.EmailField(max_length=50, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], default='O', max_length=1)),
                ('bio', models.TextField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('workplace', models.CharField(blank=True, max_length=150, null=True)),
                ('website', models.URLField(blank=True, max_length=150, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('user_timezone', timezone_field.fields.TimeZoneField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_public', models.BooleanField(default=True)),
                ('is_writer', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('type', models.IntegerField(choices=[(1, 'writer'), (2, 'admin'), (3, 'member')], default=3)),
                ('is_organization', models.BooleanField(default=False)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'myuser',
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
