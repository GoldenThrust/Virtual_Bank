# Generated by Django 4.2.7 on 2023-11-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0005_alter_merchant_business_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='api_key',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
