# Generated by Django 5.0.6 on 2024-06-07 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=10)),
                ('category', models.CharField(choices=[('Work', 'Work'), ('Personal', 'Personal'), ('Study', 'Study'), ('Other', 'Other')], default='Other', max_length=10)),
                ('state', models.CharField(choices=[('In Progress', 'In Progress'), ('Done', 'Done')], default='Open', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task_visability', models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=20)),
                ('assigned_users', models.ManyToManyField(related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_tasks', to=settings.AUTH_USER_MODEL)),
                ('state_changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state_changed_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
