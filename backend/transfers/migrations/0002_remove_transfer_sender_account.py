# Generated by Django 4.2.7 on 2023-11-22 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='sender_account',
        ),
    ]