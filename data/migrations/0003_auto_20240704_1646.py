# Generated by Django 3.2.25 on 2024-07-04 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20240704_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='автомобиль',
            options={'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='запчасти',
            options={'verbose_name_plural': 'Запчасти'},
        ),
        migrations.AlterModelOptions(
            name='страна',
            options={'verbose_name_plural': 'Страны'},
        ),
    ]
