from django.contrib import admin
from django.urls import path, include
from dashboard import views
from dashboard.views import user_profile  # Importando a função user_profile

urlpatterns = [
    path('admin/', admin.site.urls),  # Habilita o painel de administração
    path('', views.login_view, name='usuario'),  # Rota para login
    path('logout/', views.logout_view, name='logout'),  # Rota para logout
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),  # Inclui as rotas do app dashboard
    path('perfil/', user_profile, name='profile'),   # Rota para o perfil do usuário
]
