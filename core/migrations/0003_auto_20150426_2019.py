# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150426_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='locale',
            field=models.CharField(max_length=4),
        ),
    ]
