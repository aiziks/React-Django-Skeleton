# Generated by Django 3.0.2 on 2020-05-17 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='created_at',
            new_name='create_at',
        ),
    ]