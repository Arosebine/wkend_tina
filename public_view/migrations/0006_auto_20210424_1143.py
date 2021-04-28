# Generated by Django 3.0.3 on 2021-04-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_view', '0005_property_property_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.FileField(blank=True, null=True, upload_to='uploads/propfile/')),
                ('biography', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]