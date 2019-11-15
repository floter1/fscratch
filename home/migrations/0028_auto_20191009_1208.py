# Generated by Django 2.2.1 on 2019-10-09 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20191009_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='photo',
        ),
        migrations.AddField(
            model_name='members',
            name='photo1',
            field=models.ImageField(blank=True, default='avatars/default/default.jpg', null=True, upload_to='image/member/'),
        ),
    ]
