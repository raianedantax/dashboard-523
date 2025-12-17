from django.urls import path
from . import views

# Define um namespace para as URLs desta aplicação, facilitando a referência nos templates.
app_name = 'dashboard_app'

urlpatterns = [
    # Mapeia a URL raiz da aplicação para a view `consulta_boletim`.
    # Ex: http://127.0.0.1:8000/dashboard/
    path('', views.dashboard_view, name='dashboard'),
    path('consulta', views.consulta_boletim, name='consulta_boletim'),
    path('importar2', views.importacao_excel, name='importacao_excel'),
    path('importar', views.importar_mapa_notas, name='importar_mapa_notas'),

    
]