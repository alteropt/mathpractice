# Generated by Django 3.1.6 on 2021-08-15 11:56

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='date',
        ),
    ]
