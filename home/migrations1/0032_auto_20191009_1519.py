# Generated by Django 2.2.1 on 2019-10-09 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20191009_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.TextField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
    ]
