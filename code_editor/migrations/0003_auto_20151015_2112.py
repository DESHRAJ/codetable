# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_editor', '0002_auto_20151015_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesubmission',
            name='code',
            field=models.TextField(default=b"print 'Hello World'"),
        ),
    ]
