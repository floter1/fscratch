# Generated by Django 2.2.1 on 2019-10-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20191009_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origprice',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
