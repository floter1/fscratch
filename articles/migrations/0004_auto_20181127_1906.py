# Generated by Django 2.1.3 on 2018-11-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20181119_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(max_length=250),
        ),
    ]