# Generated by Django 3.1.3 on 2020-12-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanicfinder', '0009_business_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
