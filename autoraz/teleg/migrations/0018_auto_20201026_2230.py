# Generated by Django 2.2 on 2020-10-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleg', '0017_auto_20201026_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num',
            field=models.TextField(blank=True, default='', verbose_name='Кол. интимок'),
        ),
        migrations.AddField(
            model_name='user',
            name='num1',
            field=models.TextField(blank=True, default='', verbose_name='Кол. интимок'),
        ),
        migrations.AddField(
            model_name='user',
            name='num2',
            field=models.TextField(blank=True, default='', verbose_name='Кол. интимок'),
        ),
        migrations.AddField(
            model_name='user',
            name='num3',
            field=models.TextField(blank=True, default='', verbose_name='Кол. интимок'),
        ),
        migrations.AddField(
            model_name='user',
            name='num4',
            field=models.TextField(blank=True, default='', verbose_name='Кол. интимок'),
        ),
        migrations.AddField(
            model_name='user',
            name='nums',
            field=models.TextField(blank=True, default='', verbose_name='Кол. нюдсов'),
        ),
        migrations.AddField(
            model_name='user',
            name='nums1',
            field=models.TextField(blank=True, default='', verbose_name='Кол. нюдсов'),
        ),
        migrations.AddField(
            model_name='user',
            name='nums2',
            field=models.TextField(blank=True, default='', verbose_name='Кол. нюдсов'),
        ),
        migrations.AddField(
            model_name='user',
            name='nums3',
            field=models.TextField(blank=True, default='', verbose_name='Кол. нюдсов'),
        ),
        migrations.AddField(
            model_name='user',
            name='nums4',
            field=models.TextField(blank=True, default='', verbose_name='Кол. нюдсов'),
        ),
    ]
