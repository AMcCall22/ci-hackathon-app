from django.shortcuts import render
from hackathon.models import HackTeam, Hackathon
from .models import Teams
from accounts.models import Profile
from django.contrib.auth.models import User

# @login_required
def view_all_teams(request):
    """ A view to show all teams to staff """
    """ If logged in as staff identifed using 'is_staff: <BooleanField> = True'"""
    """ Team Names """

    hackathons = Hackathon.objects.all()
    teams = HackTeam.objects.all()
    participants = HackTeam.objects.filter(participant=participants)

    context = {
        'teams': teams,
        'hackathons': hackathons,
        'participants': participants,
        

                   
    }

    return render(request ,'teams/teams.html', context)

# # @login_required
# def view_individual_team(request):
#     """ A view to show a participant their own team """
#     """ Uses created_by: User to identify individual participant and is_staff: <BooleanField> = False """

#     team = Team.objects.get(pk=1)

#     return render(request ,'teams/teams.html')