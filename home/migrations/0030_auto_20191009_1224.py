# Generated by Django 2.2.1 on 2019-10-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20191009_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='photo1',
        ),
        migrations.AddField(
            model_name='members',
            name='photos1',
            field=models.ImageField(blank=True, null=True, upload_to='image/member/'),
        ),
    ]