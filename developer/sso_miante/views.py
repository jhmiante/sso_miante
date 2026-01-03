from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import SsoMiante

def sso_status(request):
    return HttpResponse("SSO Miante instalado e funcionando.")


def sso_admin(request):
    id, secrets = SsoMiante.CREATE_HASHS()
    if request.method == 'POST':
        nome = request.POST.get('nome_app')
        SsoMiante.CREATE(id, secrets, nome)

    apps = SsoMiante.objects.all()
    context = {'id_app': id, 'secrets': secrets, 'apps': apps}
    return render(request, 'sso/admin.html', context)


def sso_ativar_desativar(request, pk):
    obj = SsoMiante.objects.get(pk=pk)
    if obj.ativo: obj.ativo = False
    else: obj.ativo = True
    obj.save()
    return redirect('sso_admin')


@csrf_exempt
def sso_userinfo(request):
    dados = {}
    try:
        if request.method == 'POST':
            dados_json = request.body.decode('utf-8')            
            dados = json.loads(dados_json)
            
            # Verificando Permissões
            sso_id      = dados.get('sso_id', '-')
            sso_secrets = dados.get('sso_secrets', '-')
            username    = dados.get('username', '-')
            password    = dados.get('password', '-')

            dados = SsoMiante.AUTHENTICATE(sso_id, sso_secrets, username, password)

    except Exception as e:
        dados = {'status': 203, 'mensagem': f'ERRO: {e.args[0]}'}

    return HttpResponse(
        json.dumps(dados, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

