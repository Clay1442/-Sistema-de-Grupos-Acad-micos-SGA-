from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Club, Membership, Project, Event
# Create your views here.
@login_required
def club_list(request):
    
    user_logged = request.user
    
    clubs_advisor = user_logged.advised_clubs.all().order_by('name')

    member_clubs = user_logged.joined_clubs.exclude(pk__in=clubs_advisor).order_by('name')

    context = {
        'clubs_advisor': clubs_advisor,
        'member_clubs': member_clubs,
    }
    return render(request, 'clubs/club_list.html', context)

@login_required
def club_detail(request, pk):

    club = get_object_or_404(Club, pk=pk)

    projects = club.projects.all().order_by('-start_date')

    events = club.events.all().order_by('-event_date')

    members =   Membership.objects.filter(club=club).order_by('user__first_name')

    context = {
        'club': club,
        'projects': projects,
        'events': events,
        'members': members,
    }
    return render(request, 'clubs/club_detail.html', context)