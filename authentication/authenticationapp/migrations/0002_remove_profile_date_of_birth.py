# Generated by Django 3.0.4 on 2020-04-10 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
    ]
