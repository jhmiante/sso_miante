from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login

from .forms import UpdatePasswordForm

@login_required(login_url='login')
def UpdatePasswordView(request):
    template_name = 'update_password.html'
    form = UpdatePasswordForm(request.POST or None)
    context = {'form': form}
    user = request.user

    if user.check_password('@Drogal12'):
        context['senha_padrao'] = True

    if request.method == 'POST':
        try:
            form.atualizar(user)
            messages.success(request, 'Senha Atualizada com Sucesso!!!')
            login(request, user)
            return redirect('index')
        except Exception as e:
            messages.error(request, e.args[0])

    return render(request, template_name, context)

