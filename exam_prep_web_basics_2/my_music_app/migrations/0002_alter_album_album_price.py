# Generated by Django 4.1.4 on 2022-12-15 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
