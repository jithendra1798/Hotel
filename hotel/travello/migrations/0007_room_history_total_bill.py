# Generated by Django 3.0.5 on 2021-11-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_auto_20211105_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_history',
            name='total_bill',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
