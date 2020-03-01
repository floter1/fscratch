# Generated by Django 2.2.1 on 2020-01-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=250)),
                ('teacher_name', models.CharField(max_length=250)),
                ('student_name', models.CharField(max_length=250)),
                ('student_score', models.CharField(max_length=250)),
                ('room', models.CharField(max_length=250)),
                ('date_sched', models.CharField(max_length=250)),
                ('time_sched', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='section',
            old_name='age',
            new_name='max_students',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='last_name',
            new_name='teacher_name',
        ),
        migrations.RemoveField(
            model_name='section',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='room',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='schedule',
        ),
        migrations.AddField(
            model_name='students',
            name='guardian',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='section',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='units',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='age',
            field=models.IntegerField(blank=True, default=18, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(blank=True, default=4, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(blank=True, default=18, null=True),
        ),
    ]
