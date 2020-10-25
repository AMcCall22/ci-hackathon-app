from django.db import models
from hackathon.models import HackTeam, Hackathon
from accounts.models import Profile
from django.contrib.auth.models import User

class Teams(models.Model):
    """Model that shows Hackathon Name, Team Names, Participants and Slack IDs"""
    hackathon_display_name = Hackathon.display_name
    team_display_name = HackTeam.display_name

    def __str__(self):
            return self.display_name






