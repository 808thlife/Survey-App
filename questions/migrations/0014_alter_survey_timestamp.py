# Generated by Django 5.0.3 on 2024-05-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_alter_survey_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
