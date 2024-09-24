from django.db import models

# Classes são modelos de dados
# Cada classe é uma tabela no banco de dados
# Cada atributo da classe é uma coluna na tabela
# Cada objeto da classe é uma linha na tabela
# Cada objeto da classe é uma instância da classe



# Create your models here.
class Cadastro(models.Model): # Classe Cadastro que herda de models.Model
    nome = models.CharField(max_length=50) 
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50) 
    data = models.DateTimeField(auto_now_add=True) # auto_now_add=True é um parâmetro que faz com que a data seja preenchida automaticamente com a data atual

    def __str__(self): # Método que retorna uma representação em string do objeto
        return f'{self.nome} [{self.email}]' # Retorna o nome e o email do cadastro

    class Meta: # Meta é uma classe interna que define metadados do modelo, como o nome do modelo no singular e no plural
        verbose_name = 'Formulário de Contato' # Nome do modelo no singular
        verbose_name_plural = 'Formulários de Contato' # Nome do modelo no plural
        ordering = ['-data'] # Ordena os cadastros pela data de forma decrescente
