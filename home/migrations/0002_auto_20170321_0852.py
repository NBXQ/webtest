# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='age',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='test',
            name='hobby',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
