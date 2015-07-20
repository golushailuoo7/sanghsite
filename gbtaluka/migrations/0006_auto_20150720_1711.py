# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gbtaluka', '0005_auto_20150720_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shakha',
            name='shakha_type',
            field=models.CharField(max_length=20, choices=[('MORNING', 'Morning'), ('EVENING', 'Evening'), ('NIGHT', 'Night'), ('WEEKLY_MORNING', 'Weekly morning'), ('WEEKLY_EVENING', 'Weekly evening'), ('WEEKLY_NIGHT', 'Weekly night')]),
        ),
    ]
