# Generated by Django 4.2.2 on 2023-06-14 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='due',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
