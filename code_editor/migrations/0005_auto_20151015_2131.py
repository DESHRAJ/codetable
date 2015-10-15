# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import code_editor.models


class Migration(migrations.Migration):

    dependencies = [
        ('code_editor', '0004_auto_20151015_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesubmission',
            name='id',
            field=models.CharField(default=code_editor.models.id_generator, max_length=6, serialize=False, editable=False, primary_key=True),
        ),
    ]
