from django import forms
from .models import Club, Event, Project
from django.forms.widgets import ClearableFileInput

class CustomImageWidget(ClearableFileInput):
    initial_text = '' 
    input_text = '' 
    clear_checkbox_label = 'Remover imagem atual' 
    template_with_initial = '%(clear_template)s <br> %(input_template)s'

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'logo']
        
        widgets = {
            'logo': CustomImageWidget(),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'location']        

        widgets = {
            'event_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            )
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'objective', 'status', 'start_date', 'end_date']
            
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
        }        


class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['status']        