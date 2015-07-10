# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gbtaluka.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gbtaluka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to=gbtaluka.models.content_file_name, blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='date of birth', blank=True)),
                ('contact_number', models.CharField(null=True, max_length=10, blank=True)),
                ('blood_group', models.CharField(null=True, max_length=3, choices=[('O-', 'O Minus'), ('O+', 'O Plus'), ('A-', 'A Minus'), ('A+', 'A Plus'), ('B-', 'B Minus'), ('B+', 'B Plus'), ('AB-', 'AB Minus'), ('AB+', 'AB Plus')], blank=True)),
                ('address', models.CharField(null=True, max_length=400, blank=True)),
                ('education', models.CharField(null=True, max_length=200, blank=True)),
                ('occupation', models.CharField(null=True, max_length=200, blank=True)),
                ('hobbies', models.CharField(null=True, max_length=300, blank=True)),
                ('joining_date', models.DateField(null=True, verbose_name='date joined', blank=True)),
                ('source_of_joining', models.CharField(null=True, max_length=10, choices=[('JOINRSS', 'Through Join Rss'), ('FRIENDS', 'Through Friends'), ('FAMILY', 'Through Family'), ('SCHOOL', 'Through School/Collage'), ('OTHER', 'Any other source')], blank=True)),
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
                ('gatnayak', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='gatnayak')),
                ('responsibility', models.ForeignKey(blank=True, null=True, to='gbtaluka.Responsibility')),
                ('shakha', models.ForeignKey(blank=True, null=True, to='gbtaluka.Shakha')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='basicdetail',
            name='gatnayak',
        ),
        migrations.RemoveField(
            model_name='basicdetail',
            name='responsibility',
        ),
        migrations.RemoveField(
            model_name='basicdetail',
            name='shakha',
        ),
        migrations.RemoveField(
            model_name='basicdetail',
            name='user',
        ),
        migrations.AlterField(
            model_name='familydetail',
            name='basic_detail',
            field=models.ForeignKey(to='gbtaluka.UserDetail'),
        ),
        migrations.DeleteModel(
            name='BasicDetail',
        ),
    ]
