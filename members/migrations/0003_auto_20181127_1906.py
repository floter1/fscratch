# Generated by Django 2.1.3 on 2018-11-27 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='email',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='members',
            name='password',
        ),
    ]
