# Generated by Django 2.2.24 on 2023-05-29 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20230529_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='image',
            new_name='photo',
        ),
    ]