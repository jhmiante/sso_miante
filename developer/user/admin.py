from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm

@admin.register(Usuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = Usuario
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    
    # Configurando os fieldsets de forma adequada
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'tipo')}),  # Inclua 'password' aqui se o modelo possuir
        ('Informações Pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões Globais', {'fields': ('is_staff', 'is_active')}),
        ('Outras Permissões e Grupos', {'fields': ('groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Configuração ao adicionar um novo usuário
    add_fieldsets = (
        ('Informações Pessoais', {
            'classes': ('wide',), # collapse
            'fields': ('first_name', 'last_name', 'email', 'tipo'),
        }),
        ('Informações de Acesso', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
