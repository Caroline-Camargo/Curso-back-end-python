from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro

# Todas telas do sistema é representada por uma view
# Uma view é uma função que recebe uma requisição e retorna uma resposta
# Uma requisição é um pedido de um cliente para o servidor
# Uma resposta é a resposta do servidor para o cliente


# A função HttpResponse retorna uma resposta com o texto Hello World
def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
   
    if form.is_valid():
        sucesso = True
        form.save()

    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)
