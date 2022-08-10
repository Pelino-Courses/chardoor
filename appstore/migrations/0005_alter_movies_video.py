# Generated by Django 4.0.6 on 2022-08-08 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0004_alter_movies_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='video',
            field=models.FileField(upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]