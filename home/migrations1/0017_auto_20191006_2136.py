# Generated by Django 2.2.1 on 2019-10-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191006_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
