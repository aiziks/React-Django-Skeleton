# Generated by Django 3.0.2 on 2020-05-24 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0007_auto_20200524_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='owner',
        ),
    ]
