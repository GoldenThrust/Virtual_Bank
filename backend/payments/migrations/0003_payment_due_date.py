# Generated by Django 4.2.7 on 2023-11-23 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_payment_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 3, 16, 19, 679186)),
        ),
    ]