# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20151130_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='extraordinario',
            field=models.IntegerField(choices=[(1, b'Si'), (0, b'No')]),
        ),
    ]
