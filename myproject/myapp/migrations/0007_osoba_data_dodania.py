# Generated by Django 5.1.1 on 2025-01-27 19:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_osoba_data_dodania'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]