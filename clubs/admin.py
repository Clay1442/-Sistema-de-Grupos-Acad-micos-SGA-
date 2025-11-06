from django.contrib import admin
from .models import Club, Membership, Event, Project

class MembershipInline(admin.TabularInline):
    model = Membership 
    extra = 1          
    autocomplete_fields = ('user',) 

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'advisor', 'created_at')
    list_filter = ('advisor',)
    search_fields = ('name', 'description')
    
    
    autocomplete_fields = ('advisor',)
    
   
    inlines = [MembershipInline]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'event_date', 'location')
    list_filter = ('club', 'event_date')
    search_fields = ('title', 'description')
    autocomplete_fields = ('club',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'status', 'start_date')
    list_filter = ('status', 'club')
    search_fields = ('title', 'objective')
    autocomplete_fields = ('club',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'club', 'position', 'input_date')
    list_filter = ('club', 'position')
    autocomplete_fields = ('user', 'club')
