# Generated by Django 5.1.6 on 2025-04-18 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_film_unique_together_userfilm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='mois_sortie',
        ),
    ]
