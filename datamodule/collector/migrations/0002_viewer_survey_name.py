# Generated by Django 3.2.5 on 2021-08-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewer',
            name='survey_name',
            field=models.CharField(default='kavtech', max_length=50),
        ),
    ]
