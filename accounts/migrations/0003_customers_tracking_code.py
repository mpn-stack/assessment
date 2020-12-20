# Generated by Django 2.2 on 2020-12-15 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customers_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='tracking_code',
            field=models.IntegerField(auto_created=True, null=True, validators=[django.core.validators.MinValueValidator(10000)]),
        ),
    ]
