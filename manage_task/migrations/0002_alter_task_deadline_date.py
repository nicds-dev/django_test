# Generated by Django 4.2.7 on 2023-11-29 01:01

from django.db import migrations, models
import manage_task.models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(validators=[manage_task.models.limit_date], verbose_name='Task deadline date'),
        ),
    ]
