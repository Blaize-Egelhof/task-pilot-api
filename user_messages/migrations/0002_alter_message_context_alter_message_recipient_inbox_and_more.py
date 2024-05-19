# Generated by Django 5.0.6 on 2024-05-19 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_initial'),
        ('task', '0002_initial'),
        ('user_messages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='context',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient_inbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inbox.inbox'),
        ),
        migrations.AlterField(
            model_name='message',
            name='related_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
