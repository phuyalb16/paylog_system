# Generated by Django 2.1.7 on 2019-06-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paylog_app', '0006_auto_20190616_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='amount',
            field=models.FloatField(),
        ),
    ]
