# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pontos', '0003_registro_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='ip_address',
            field=models.CharField(default=b'ABC', max_length=120),
            preserve_default=True,
        ),
    ]
