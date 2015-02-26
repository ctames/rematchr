# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rematchrApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='conference',
            field=models.ForeignKey(default='', to='rematchrApp.Conference'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='doc_texts',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='doc_urls',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
