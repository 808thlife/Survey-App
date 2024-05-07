# Generated by Django 5.0.3 on 2024-05-06 17:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answer', models.TextField()),
                ('is_answered', models.BooleanField()),
                ('all', models.BooleanField()),
                ('expired', models.BooleanField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('organisations', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]