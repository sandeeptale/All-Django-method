# Generated by Django 4.1.3 on 2022-11-17 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='passby',
        ),
    ]
