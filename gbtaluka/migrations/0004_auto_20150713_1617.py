# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gbtaluka', '0003_auto_20150710_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='gatnayak',
            field=models.ForeignKey(blank=True, related_name='gatnayak_fk', to='gbtaluka.UserDetail', null=True),
        ),
    ]
