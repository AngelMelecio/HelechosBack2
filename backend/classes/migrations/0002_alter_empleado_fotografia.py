# Generated by Django 4.1.4 on 2022-12-22 19:01

import classes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fotografia',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=classes.models.upload_to),
        ),
    ]
