# Generated by Django 2.1.5 on 2019-11-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20191119_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='image',
            field=models.ImageField(upload_to='topping_img2/'),
        ),
    ]
