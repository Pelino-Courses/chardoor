# Generated by Django 4.0.6 on 2022-08-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0003_remove_addmovie_url_alter_movies_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='released_date',
            field=models.DateField(),
        ),
    ]