# Generated by Django 3.1.1 on 2021-04-24 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_view', '0007_auto_20210424_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactagent',
            name='property_id',
        ),
    ]