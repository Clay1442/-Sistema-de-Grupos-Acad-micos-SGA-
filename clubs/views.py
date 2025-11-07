from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Club

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