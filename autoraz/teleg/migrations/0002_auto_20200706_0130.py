# Generated by Django 3.1b1 on 2020-07-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='telegram_id'),
        ),
    ]
