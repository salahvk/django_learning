# Generated by Django 5.0.1 on 2024-02-26 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_movieinfo_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='directed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_movies', to='movieapp.director'),
        ),
    ]
