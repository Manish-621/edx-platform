# Generated by Django 3.2.17 on 2023-03-20 12:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0046_alter_userregistration_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 12, 23, 45, 412643, tzinfo=utc)),
        ),
    ]
