from django import forms
from .models import Club
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