# Generated by Django 4.0.1 on 2022-07-27 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthdate',
            field=models.DateTimeField(),
        ),
    ]
