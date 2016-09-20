# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftunes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('ALTERNATIVE', 'alternative'), ('DISCO', 'disco'), ('JAM_BAND', 'jam band'), ('ROCK', 'rock'), ('POP', 'pop'), ('BAD', 'bad'), ('GOOD', 'good')], default='good', max_length=50),
        ),
    ]
