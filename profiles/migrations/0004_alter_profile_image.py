# Generated by Django 5.0.6 on 2024-06-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_qsg0aq', upload_to='images/'),
        ),
    ]