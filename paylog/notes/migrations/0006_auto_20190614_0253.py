# Generated by Django 2.1.7 on 2019-06-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20190614_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makenotes',
            name='Text',
        ),
        migrations.AddField(
            model_name='makenotes',
            name='note',
            field=models.CharField(default='', max_length=200),
        ),
    ]
