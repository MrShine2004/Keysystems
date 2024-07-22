# Generated by Django 3.2.25 on 2024-07-04 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=3)),
                ('capital', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.country'),
        ),
    ]
