# São as importações realizadas de forma a utilizar partes do django.
from django.urls import path
# Importação do diretório views, onde tem a view index e a view listarPacientes
from sistema import views

app_name = 'sistema'

# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listarPacientes, name='listar'),
    path('medicos/', views.listarMedicos, name='listar')
]

# path() é um método do django que permite realizar a inserção de um url