# Generated by Django 3.1.1 on 2020-10-26 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0017_auto_20201025_2004'),
        ('teams', '0006_teams_hackathons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='hackathons',
        ),
        migrations.AddField(
            model_name='teams',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='team_description',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='team_members',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='team_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='hackathon.hackteam'),
        ),
    ]
