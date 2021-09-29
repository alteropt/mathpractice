# Generated by Django 3.1.6 on 2021-08-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210815_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ('-date',), 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]