# Generated by Django 5.0.3 on 2024-05-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_survey_next_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='next_schedule',
            field=models.DateTimeField(),
        ),
    ]
