# Generated by Django 4.2.11 on 2024-03-13 06:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fearured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
