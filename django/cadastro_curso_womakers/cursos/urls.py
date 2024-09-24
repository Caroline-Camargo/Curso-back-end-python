from django.urls import path
from cursos.views import criar_curso

app_name = 'cursos'
urlpatterns = [
    path('criar_curso/', criar_curso, name='criar_curso'),
]
