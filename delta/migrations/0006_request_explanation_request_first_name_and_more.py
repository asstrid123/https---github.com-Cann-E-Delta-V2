# Generated by Django 5.1.6 on 2025-03-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0005_remove_request_date_updated_and_more'),
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
    ]
