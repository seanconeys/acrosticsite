# Generated by Django 2.2.3 on 2019-07-12 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acrostic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acrostic',
            name='root_word',
            field=models.TextField(max_length=50),
        ),
    ]
