# São as importações realizadas de forma a se utilizar partes do django
from django.urls import path
from sistema import views
# Lista responsável por organizar as urls do sistema
urlpatterns = [
    path ('noah/', views.noah),
]

# path() é um método do django que permite realizar a inserção de um url