from django.db import models
from django.utils import timezone

class usuarios(models.Model):
    nome = models.CharField(max_length=50,blank=True)
    sobrenome = models.CharField(max_length=100,blank=True)
    cpf = models.CharField(max_length=14, blank= True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField(max_length=8)
    data_criacao = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=20, blank=True)
    senha = models.CharField(max_length=16,blank=True)
    inativo = models.BooleanField(default=False)
    