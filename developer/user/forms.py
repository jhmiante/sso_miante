from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email']


class UpdatePasswordForm(forms.Form):
    senha_atual = forms.CharField(
        label='Senha Atual', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha atual',
            }
        ),
    )

    senha_nova = forms.CharField(
        label='Nova Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha nova',
            }
        ),
    )
    
    senha_conferencia = forms.CharField(
        label='Confirme Nova Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha novamente',
            }
        ),
    )

    def atualizar(self, user:Usuario):
        if self.is_valid():
            senha_atual = self.cleaned_data['senha_atual']
            senha_nova = self.cleaned_data['senha_nova']
            
            if senha_atual == senha_nova:
                raise Exception('Senha Nova não pode ser igual a Senha Atual')
            
            elif not user.check_password(senha_atual):
                raise Exception('Senha Atual está incorreta!!!')
            
            else:        
                user.set_password(senha_nova)
                user.save()
        else:
            raise Exception('Erro ao alterar a senha')
    

    def clean_senha_conferencia(self):
        senha_nova = self.cleaned_data['senha_nova']
        senha_conferencia = self.cleaned_data['senha_conferencia']

        if senha_nova and senha_conferencia:
            if senha_nova != senha_conferencia:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_conferencia


