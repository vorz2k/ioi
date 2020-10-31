# Generated by Django 2.2 on 2020-10-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleg', '0020_settings_bot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings_bot',
            options={'verbose_name': 'Настройку', 'verbose_name_plural': 'Настройки'},
        ),
        migrations.AddField(
            model_name='settings_bot',
            name='name',
            field=models.TextField(blank=True, default='karel', verbose_name='Имя'),
        ),
    ]
