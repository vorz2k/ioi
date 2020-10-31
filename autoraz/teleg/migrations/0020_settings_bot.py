# Generated by Django 2.2 on 2020-10-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleg', '0019_user_prime'),
    ]

    operations = [
        migrations.CreateModel(
            name='settings_bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_bot', models.TextField(blank=True, default='', verbose_name='Токен бота')),
            ],
            options={
                'verbose_name': 'Настройки',
                'db_table': 'telegram_token',
            },
        ),
    ]