# Generated by Django 5.0.6 on 2024-06-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmessage',
            name='context',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]