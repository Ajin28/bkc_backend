# Generated by Django 4.0.4 on 2024-12-17 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='forecast_updated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_recorded_units_sold',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]