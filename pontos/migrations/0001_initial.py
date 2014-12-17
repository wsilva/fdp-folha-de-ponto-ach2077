# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registro', models.DateTimeField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.CharField(default=b'no-image.jpg', max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
