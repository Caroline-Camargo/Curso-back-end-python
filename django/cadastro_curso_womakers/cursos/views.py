from django.shortcuts import render
from cursos.forms import CursoForm
from cursos.models import Curso
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(30) # 30 segundos de cache 
def criar_curso(request):
    cursos = Curso.objects.all()
    sucesso = False
    form = CursoForm(request.POST or None)

    if form.is_valid():
        sucesso = True
        form.save()
    
    contexto = {
        'form': form,
        'sucesso': sucesso,
        'cursos': cursos
    }

    return render(request, 'criar_curso.html', contexto)
