# Generated by Django 3.0.5 on 2021-11-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20211105_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_type',
            name='room_image1',
            field=models.ImageField(default='room_images/room_image3.jpg', upload_to='room_images'),
        ),
        migrations.AlterField(
            model_name='room_type',
            name='room_image2',
            field=models.ImageField(default='room_images/room_image1.jpg', upload_to='room_images'),
        ),
        migrations.AlterField(
            model_name='room_type',
            name='room_image3',
            field=models.ImageField(default='room_images/room_image2.jpg', upload_to='room_images'),
        ),
    ]
