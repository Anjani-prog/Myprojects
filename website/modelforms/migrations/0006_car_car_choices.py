# Generated by Django 2.0.4 on 2018-04-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelforms', '0005_auto_20180428_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_choices',
            field=models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
