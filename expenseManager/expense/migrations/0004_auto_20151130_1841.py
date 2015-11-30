# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expense_extraordinado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='extraordinado',
            new_name='extraordinario',
        ),
    ]
