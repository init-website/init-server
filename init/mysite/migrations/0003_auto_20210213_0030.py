# Generated by Django 3.1.5 on 2021-02-13 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210212_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inituser',
            name='student_number',
        ),
        migrations.AlterField(
            model_name='inituser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='inituser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='inituser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
