# Generated by Django 4.0.1 on 2022-03-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_rename_trips_tripss'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetails',
            name='writer',
            field=models.CharField(default=models.CharField(default='', max_length=30), max_length=30),
        ),
    ]