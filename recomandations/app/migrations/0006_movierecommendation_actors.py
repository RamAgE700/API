# Generated by Django 5.0 on 2024-04-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_movierecommendation_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movierecommendation',
            name='actors',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
