# Generated by Django 4.2.7 on 2023-11-19 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0003_alter_merchant_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='private_key',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='public_key',
        ),
    ]