# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gbtaluka.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to=gbtaluka.models.content_file_name, blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='date of birth', blank=True)),
                ('contact_number', models.CharField(max_length=10, null=True, blank=True)),
                ('blood_group', models.CharField(choices=[('O-', 'O Minus'), ('O+', 'O Plus'), ('A-', 'A Minus'), ('A+', 'A Plus'), ('B-', 'B Minus'), ('B+', 'B Plus'), ('AB-', 'AB Minus'), ('AB+', 'AB Plus')], null=True, max_length=3, blank=True)),
                ('address', models.CharField(max_length=400, null=True, blank=True)),
                ('education', models.CharField(max_length=200, null=True, blank=True)),
                ('occupation', models.CharField(max_length=200, null=True, blank=True)),
                ('hobbies', models.CharField(max_length=300, null=True, blank=True)),
                ('joining_date', models.DateField(null=True, verbose_name='date joined', blank=True)),
                ('source_of_joining', models.CharField(choices=[('JOINRSS', 'Through Join Rss'), ('FRIENDS', 'Through Friends'), ('FAMILY', 'Through Family'), ('SCHOOL', 'Through School/Collage'), ('OTHER', 'Any other source')], null=True, max_length=10, blank=True)),
                ('prathmik_completed', models.BooleanField()),
                ('prathm_varsh_completed', models.BooleanField()),
                ('dwitiya_varsh_completed', models.BooleanField()),
                ('tratiya_varsh_completed', models.BooleanField()),
                ('shirt', models.BooleanField()),
                ('pants', models.BooleanField()),
                ('socks', models.BooleanField()),
                ('shoes', models.BooleanField()),
                ('cap', models.BooleanField()),
                ('belt', models.BooleanField()),
                ('bamboo_staff', models.BooleanField()),
                ('publish', models.BooleanField()),
                ('gatnayak', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='gatnayak', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('venue', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relative_name', models.CharField(max_length=200)),
                ('relation', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('blood_group', models.CharField(choices=[('O-', 'O Minus'), ('O+', 'O Plus'), ('A-', 'A Minus'), ('A+', 'A Plus'), ('B-', 'B Minus'), ('B+', 'B Plus'), ('AB-', 'AB Minus'), ('AB+', 'AB Plus')], max_length=3)),
                ('date_of_birth', models.DateField(verbose_name='date of birt')),
                ('basic_detail', models.ForeignKey(to='gbtaluka.BasicDetail')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('from_date', models.DateTimeField(verbose_name='start time')),
                ('to_date', models.DateTimeField(verbose_name='end time')),
            ],
        ),
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shakha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shakha_name', models.CharField(max_length=200)),
                ('shakha_time', models.TimeField(verbose_name='shakha time')),
                ('shakha_type', models.CharField(choices=[('MG', 'Morning'), ('EV', 'Evening'), ('NT', 'Night'), ('WM', 'Weekly morning'), ('WE', 'Weekly evening'), ('WN', 'Weekly night')], max_length=2)),
                ('shakha_venue', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='eventdetail',
            name='responsibility',
            field=models.ForeignKey(to='gbtaluka.Responsibility'),
        ),
        migrations.AddField(
            model_name='basicdetail',
            name='responsibility',
            field=models.ForeignKey(blank=True, to='gbtaluka.Responsibility', null=True),
        ),
        migrations.AddField(
            model_name='basicdetail',
            name='shakha',
            field=models.ForeignKey(blank=True, to='gbtaluka.Shakha', null=True),
        ),
        migrations.AddField(
            model_name='basicdetail',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
