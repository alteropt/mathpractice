# Generated by Django 3.2.6 on 2021-09-09 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20210909_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]