# Generated by Django 4.2.3 on 2023-07-19 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_msgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msgroup',
            old_name='category',
            new_name='mgroup_name',
        ),
    ]