from django.shortcuts import render
from .models import Club

# Create your views here.
def club_list(request):
    
    clubs = Club.objects.all().order_by('name')
    
    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs/club_list.html', context)