# Generated by Django 5.0.1 on 2024-02-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_actor_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='actors',
            field=models.ManyToManyField(related_name='acted_movies', to='movieapp.actor'),
        ),
    ]
