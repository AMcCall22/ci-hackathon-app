# Generated by Django 3.1.1 on 2020-12-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0028_auto_20201206_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='team_members',
            field=models.ManyToManyField(to='teams.Team_Members'),
        ),
    ]
