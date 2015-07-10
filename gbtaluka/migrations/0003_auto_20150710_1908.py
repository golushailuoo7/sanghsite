# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gbtaluka', '0002_auto_20150710_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='bamboo_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='belt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='cap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='dwitiya_varsh_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='pants',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='prathm_varsh_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='prathmik_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='shirt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='shoes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='socks',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='tratiya_varsh_completed',
            field=models.BooleanField(default=False),
        ),
    ]
