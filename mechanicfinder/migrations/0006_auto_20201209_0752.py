# Generated by Django 3.1.3 on 2020-12-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanicfinder', '0005_auto_20201209_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='cert',
            field=models.ImageField(default='cert.jpg', upload_to='images'),
        ),
    ]
