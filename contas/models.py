from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.nome

class Transacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField()

class Meta:
    verbose_name_plural = 'Transacoes'

    def __str__(self):
       return self.descricao

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)

class MetaC:
    verbose_name_plural = 'Cliente'

    def __str__(self):
       return self.nome