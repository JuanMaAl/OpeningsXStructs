# Generated by Django 5.1.2 on 2024-11-14 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oxs', '0007_structures_structure_map_alter_variants_structures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structures',
            name='structure_map',
        ),
    ]
