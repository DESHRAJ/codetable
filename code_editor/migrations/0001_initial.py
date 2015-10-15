# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('code', models.TextField()),
                ('language', models.CharField(default=None, max_length=4, choices=[(b'PY', b'Python'), (b'C', b'C language'), (b'C++', b'C++'), (b'JAVA', b'Java')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
