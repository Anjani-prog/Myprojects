# Generated by Django 2.0.4 on 2018-04-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelforms', '0015_auto_20180428_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_mileage',
            field=models.TextField(),
        ),
    ]
