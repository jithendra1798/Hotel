# Generated by Django 3.0.5 on 2021-11-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20211105_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_type',
            name='room_image1',
            field=models.ImageField(default='room_image3', upload_to='room_images'),
        ),
        migrations.AlterField(
            model_name='room_type',
            name='room_image2',
            field=models.ImageField(default='room_image1', upload_to='room_images'),
        ),
        migrations.AlterField(
            model_name='room_type',
            name='room_image3',
            field=models.ImageField(default='room_image2', upload_to='room_images'),
        ),
    ]
