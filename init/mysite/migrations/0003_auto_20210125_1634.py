# Generated by Django 3.1.5 on 2021-01-25 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_homework'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='Homework_submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('submitted_at', models.DateTimeField(auto_now=True)),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mysite.homework')),
            ],
        ),
    ]