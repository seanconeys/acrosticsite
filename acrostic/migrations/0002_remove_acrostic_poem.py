# Generated by Django 2.2.3 on 2019-07-10 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acrostic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acrostic',
            name='poem',
        ),
    ]