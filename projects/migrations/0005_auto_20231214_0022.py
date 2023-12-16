# Generated by Django 3.1.8 on 2023-12-13 21:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20231214_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deprem',
            name='MagnitudeEarthquake',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9.9)], verbose_name='Magnitude of The Earthquake'),
        ),
    ]
