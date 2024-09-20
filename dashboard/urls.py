from django.urls import path
from . import views

app_name = 'dashboard'  # Namespace para o app

urlpatterns = [
    path('<str:dashboard_name>/', views.dashboard_view, name='dashboard_view'),  # View do dashboard
]
