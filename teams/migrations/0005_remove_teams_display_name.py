# Generated by Django 3.1.1 on 2020-10-22 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_teams_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='display_name',
        ),
    ]