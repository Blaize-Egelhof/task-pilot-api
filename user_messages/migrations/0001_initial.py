# Generated by Django 5.0.6 on 2024-06-07 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inbox', '0001_initial'),
        ('task', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(blank=True)),
                ('declined', models.BooleanField(blank=True)),
                ('title', models.CharField(max_length=30)),
                ('context', models.CharField(max_length=50)),
                ('read_status', models.BooleanField(blank=True, default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('recipient_inbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inbox.inbox')),
                ('related_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
