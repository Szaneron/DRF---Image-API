# Generated by Django 4.1.7 on 2023-03-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
