# Generated by Django 5.1.7 on 2025-03-17 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
