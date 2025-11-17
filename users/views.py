from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    # Se o utilizador já estiver logado, redireciona-o
    if request.user.is_authenticated:
        return redirect('club-list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # O formulário trata de encriptar a password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Pode agora fazer login.')
            return redirect('login') # Redireciona para a página de login
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)