# Generated by Django 2.1.5 on 2019-11-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20191119_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='image',
            field=models.ImageField(upload_to='img/topping_img/'),
        ),
    ]
