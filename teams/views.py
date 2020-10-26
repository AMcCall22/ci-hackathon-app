from django.shortcuts import render
from hackathon.models import HackTeam, Hackathon
from .models import Teams, Team_Members
from django.contrib.auth.models import User

# @login_required
def view_all_teams(request):
    """ A view to show all teams to staff """
    """ If logged in as staff identifed using 'is_staff: <BooleanField> = True'"""
    """ Team Names """

    teams = Teams.objects.all()
    hackathon = Hackathon.objects.all()
    
    
    context = {
        'teams': teams,
        'hackathon': hackathon,
        'team_members': teams,                        
    }

    return render(request ,'teams/teams.html', context)

