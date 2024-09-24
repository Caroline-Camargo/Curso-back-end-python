from django.contrib import admin
from base.models import Cadastro

# No arquivo admin.py, importamos o modelo Cadastro e registramos ele no admin

# Register your models here.

@admin.register(Cadastro) # Registra o modelo Cadastro no admin
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data'] # Exibe o nome, email e data na lista de cadastros
    search_fields = ['nome', 'email'] # Adiciona um campo de busca para nome e email
    list_filter = ['data'] # Adiciona um filtro para data
    pass
    
