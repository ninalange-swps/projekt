# Generated by Django 5.1.1 on 2025-01-28 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_osoba_wlasciciel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'permissions': [('view_person_other_owner', 'pozwla zobaczyc modele Osoba innych wlascicieli')]},
        ),
    ]