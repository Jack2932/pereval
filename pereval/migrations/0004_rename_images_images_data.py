# Generated by Django 4.2 on 2023-04-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0003_rename_data_images_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='data',
        ),
    ]
