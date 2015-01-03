# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pontos', '0004_registro_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='ip_address',
            field=models.CharField(default=b'0.0.0.0', max_length=120),
            preserve_default=True,
        ),
    ]
