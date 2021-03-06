# Generated by Django 3.1.1 on 2021-03-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_view', '0002_auto_20210326_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='Default slug value', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
