# Generated by Django 5.0.1 on 2024-02-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]