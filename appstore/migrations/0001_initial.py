# Generated by Django 4.0.6 on 2022-08-04 15:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='AddMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('releasedDate', models.DateField()),
                ('mainActor', models.CharField(max_length=35)),
                ('Genre', models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY')], max_length=10)),
                ('moviePoster', models.ImageField(null=True, upload_to='')),
                ('url', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='addUpComing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('mainActor', models.CharField(max_length=70)),
                ('dateTobeOut', models.DateField()),
                ('Genre', models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('released_date', models.CharField(max_length=255)),
                ('main_actor', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=70)),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='other', max_length=20)),
                ('Age', models.IntegerField()),
                ('Profile', models.ImageField(upload_to='')),
                ('RegistrationDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=70)),
                ('LastName', models.CharField(max_length=70)),
                ('bio', models.TextField()),
                ('ProfilePic', models.ImageField(blank=True, null=True, upload_to='images/profiles')),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='other', max_length=20)),
                ('Age', models.IntegerField()),
                ('Profile', models.ImageField(upload_to='')),
                ('RegistrationDate', models.DateField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='appstore.user')),
            ],
        ),
    ]
