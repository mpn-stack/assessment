# Generated by Django 2.2 on 2020-12-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201215_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='tracking_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
