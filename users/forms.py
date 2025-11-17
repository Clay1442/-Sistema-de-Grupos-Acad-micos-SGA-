from django.contrib.auth.forms import UserCreationForm
from users.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User # Usa o seu modelo 'User' customizado
        
        # Campos que o utilizador vai preencher
        fields = ('username', 'first_name', 'last_name', 'email')