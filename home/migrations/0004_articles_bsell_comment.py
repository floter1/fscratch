# Generated by Django 2.2 on 2019-04-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190428_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(max_length=250)),
                ('writer', models.CharField(max_length=250)),
                ('points', models.FloatField(blank=True, default=0.0, null=True)),
                ('like', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bsell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('owner', models.CharField(default='admin', max_length=250)),
                ('coins', models.FloatField(blank=True, default=0.0, null=True)),
                ('price', models.FloatField(blank=True, default=1.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=250)),
                ('like', models.FloatField(blank=True, default=0.0, null=True)),
                ('points', models.FloatField(blank=True, default=0.0, null=True)),
                ('author', models.CharField(max_length=250)),
                ('commentor', models.CharField(max_length=250)),
            ],
        ),
    ]
