# Generated by Django 4.1.3 on 2022-11-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stupid', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('stupas', models.CharField(max_length=70)),
                ('Comment', models.CharField(default='not available', max_length=40)),
            ],
        ),
    ]