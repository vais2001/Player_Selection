# Generated by Django 4.2.9 on 2024-01-17 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='Skillname',
        ),
    ]