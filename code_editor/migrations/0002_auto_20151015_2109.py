# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_editor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesubmission',
            name='code',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='codesubmission',
            name='language',
            field=models.CharField(default=b'PY', max_length=4, choices=[(b'PY', b'Python'), (b'C', b'C language'), (b'C++', b'C++'), (b'JAVA', b'Java')]),
        ),
    ]
