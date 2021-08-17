# Generated by Django 3.2.5 on 2021-08-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_viewer_survey_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestap', models.FloatField()),
                ('emotion', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='viewer',
            name='survey_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]