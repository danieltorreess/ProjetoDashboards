from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django import forms

# View para login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

# Formulário de perfil
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

@login_required
def user_profile(request):
    if request.method == 'POST':
        # Atualizando informações do usuário
        user = request.user
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        # Atualizando a senha, se fornecida
        if request.POST['old_password'] and request.POST['new_password']:
            if user.check_password(request.POST['old_password']):
                if request.POST['new_password'] == request.POST['new_password_confirmation']:
                    user.set_password(request.POST['new_password'])
                    user.save()
                    # Redirecionar para a tela de login após alteração de senha
                    return redirect('logout')
                else:
                    # Caso as senhas não coincidam
                    return render(request, 'profile.html', {'error': 'As novas senhas não coincidem.'})
            else:
                # Senha atual incorreta
                return render(request, 'profile.html', {'error': 'Senha atual incorreta.'})

        # Redireciona para a página do dashboard após salvar
        return redirect('dashboard:dashboard_view', dashboard_name='arafarialima')

    return render(request, 'profile.html')


@never_cache
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)  # Busca o usuário pelo e-mail
            user = authenticate(request, username=user.username, password=password)  # Autentica usando o nome de usuário
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard:dashboard_view', dashboard_name='arafarialima')
            else:
                messages.error(request, 'Login ou senha incorretos...')  # Usa o sistema de mensagens para mostrar o erro
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')  # Usa o sistema de mensagens para mostrar o erro
    return render(request, 'usuario.html')


# View para logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('usuario')

# View para exibir os dashboards, protegida por login
@login_required
def dashboard_view(request, dashboard_name):
    dashboards = {
            'arafarialima': {
                'title': 'Ara Faria Lima',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiYzFhMzJmODEtZGMyZS00NmE3LTgxYmYtNDRlYmI5NDM0NDRiIiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'chamados_ti': {
                'title': 'Chamados T.I',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiOTRkZTllNDMtY2QyNS00ZDJlLTgxNDktODNhNjhlZDk4MTEyIiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'dp_rh': {
                'title': 'DP - RH',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiZDM4ZDEyODItOGIxZS00MmY4LThhZjktYTEyZjgxZDhkZjc4IiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'financeiro_mv': {
                'title': 'Financeiro MV',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiOWQ4ZGVjZGYtMDlmNC00NGRjLWFhMDEtNWQ1YjY1ZTI1ZTYzIiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'financeiro_gerenciamento': {
                'title': 'Financeiro Gerenciamento',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiMzc3ZWJkYjQtZGUyMC00NTkwLWE4NmMtYTQzM2RmNWIxZjU3IiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'financeiro_visna': {
                'title': 'Financeiro Visna',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiNjI1MmFhY2EtZTJhYS00NzE4LThkYWQtZmIxNmQ5N2IxNWE1IiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'indicadores': {
                'title': 'Indicadores financeiros',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiNDE2OWZjMGItNDQ4MC00ZDFjLTlmZGYtNWIyZDQ4MWE0Y2E0IiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'processos_mv': {
                'title': 'Processos MV',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiN2NhYzIxMDMtNWQ0OC00NjhiLWE4ZjYtOTU3ZGMxNzM2Y2I1IiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'suprimentos': {
                'title': 'Suprimentos',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiYmQ2ODJjZWEtOTJmYy00MGMzLTgyNzQtMWJiZWFkMGIyYWMxIiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'indices': {
                'title': 'Índices',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiNzhmZmRkODktODY4My00MGUwLTgyNzktNWI3ZTZkNDVlMzU4IiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            'quadro_oferta': {
                'title': 'Quadro de oferta',
                'iframe_src': 'https://app.powerbi.com/view?r=eyJrIjoiZjIwYWNkYjktM2RhZi00ZDk2LWE5ZDYtNzczNDM0MmRlYzFjIiwidCI6IjM2YTcwOGM2LWEwYzgtNDYyYy05MjE1LWY2YzI3ZGNiNjZhMCJ9'
            },
            # Adicione mais dashboards conforme necessário
        }
    
    if dashboard_name in dashboards:
        context = dashboards.get(dashboard_name)  # Usa get() para evitar KeyError
        return render(request, 'powerbi.html', context)
    else:
        return redirect('usuario')
  # Redireciona para login se o dashboard não existir
