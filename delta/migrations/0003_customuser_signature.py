# Generated by Django 5.1.6 on 2025-03-15 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0002_remove_customuser_signature_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='signatures/'),
        ),
    ]
