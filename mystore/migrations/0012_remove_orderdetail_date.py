# Generated by Django 3.1.4 on 2020-12-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0011_auto_20201219_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='date',
        ),
    ]
