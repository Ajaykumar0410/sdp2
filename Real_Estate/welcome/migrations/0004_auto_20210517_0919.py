# Generated by Django 3.2.3 on 2021-05-17 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_auto_20210516_2038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
