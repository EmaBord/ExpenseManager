# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='rode',
            new_name='precio',
        ),
    ]
