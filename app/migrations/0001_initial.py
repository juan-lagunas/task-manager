# Generated by Django 4.2.2 on 2023-06-14 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=64)),
                ('note', models.CharField(max_length=128)),
                ('created', models.DateField(default=datetime.date(2023, 6, 14))),
                ('due', models.DateField(default=datetime.date(2023, 6, 14))),
                ('complete', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
