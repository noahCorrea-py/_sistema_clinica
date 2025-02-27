# São as importações realizadas de forma a se utilizar partes do django
from django.contrib import admin
from django.urls import path

# Lista responsável por organizar as urls do sistema
urlpatterns = [
    path('admin/', admin.site.urls),
]

# path() é um método do django que permite realizar a inserção de um url
