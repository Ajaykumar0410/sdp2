# Generated by Django 3.2.3 on 2021-05-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_auto_20210517_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30, null=True)),
                ('lname', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
