# Generated by Django 5.0.1 on 2024-01-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
