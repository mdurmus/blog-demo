# Generated by Django 4.2.11 on 2024-03-13 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_fearured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='fearured_image',
            new_name='featured_image',
        ),
    ]