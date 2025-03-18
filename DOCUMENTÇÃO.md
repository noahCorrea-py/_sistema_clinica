# DJANGO

# COMANDOS PRINCIPAIS

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> venv\Scripts\activate
3. Instalar o django no projeto -> pip install django
4. Para criar um projeto Django -> django-admin startproject project .
5. Para subir o servidor -> python manage.py runserver
6. Para criar um novo app -> python manage.py startapp sistema
7. Para criar um superuser -> python manage.py createsuperuser
8. Para alterar a senha, caso você esqueça -> python manage.py changepassword nomedousuario
9. Para instalar o pillow no projeto -> python -m pip install Pillow
10. Para gerar o pacote de migração -> python manage.py makemigrations
11. Para rodar as alterações desse pacote -> python manage.py migrate

# PRINCIPAIS ARQUIVOS/PASTAS DO PROJECT
1. setting.py -> é o arquivo de configuração do projeto
2. urls.py -> é o arquivo base [principal] de urls do projeto

# DOCUMENTAÇÃO
1. `urls` -> https://docs.djangoproject.com/en/5.1/topics/http/urls/
2. `settings` -> https://docs.djangoproject.com/en/5.1/topics/settings/, https://docs.djangoproject.com/en/5.1/ref/settings/

# CRIAÇÃO DAS ENTIDADES DO SISTEMA

[PACIENTE] 
- nome 
- sobrenome 
- email 
- telefone 
- criação 
- mensagem 
- ativo 
- imagem

[ESPECIALIDADE] 
- ortopedia 
- cardiologia 
- neurologia 
- clinico 
- geral

[MEDICO] 
- nome 
- sobrenome 
- crm 
- email 
- data do cadastro do médico 
- telefone 
- imagem 
- ativo 
- mensagem

[CONSULTA]

[ENDEREÇO]