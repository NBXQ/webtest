# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170321_0852'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='User',
        ),
    ]
