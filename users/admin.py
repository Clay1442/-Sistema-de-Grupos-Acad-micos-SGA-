from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Importa seu modelo User

# Cria uma classe de admin customizada
class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos na lista de usuários
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
    # Adiciona 'user_type' aos filtros
    list_filter = UserAdmin.list_filter 

    # Adiciona seus campos customizados à tela de edição do usuário
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('identifier', 'profile_photo', 'bio')
        }),
    )
    
    # Adiciona seus campos customizados à tela de criação de usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('identifier', 'profile_photo', 'bio')
        }),
    )

# Registra seu modelo User com a classe customizada
admin.site.register(User, CustomUserAdmin)