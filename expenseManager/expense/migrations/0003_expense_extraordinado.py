# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20151127_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='extraordinado',
            field=models.BooleanField(default=datetime.datetime(2015, 11, 30, 18, 40, 12, 127165, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
