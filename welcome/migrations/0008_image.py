# Generated by Django 3.2.3 on 2021-05-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
