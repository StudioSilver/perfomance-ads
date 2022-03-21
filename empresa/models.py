from django.db.models.fields import CharField, EmailField, TextField
from django.core.validators import RegexValidator, MinLengthValidator
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse

# Create your models here.

class Empresa(models.Model):

    STATUS = (
        ('on', 'Ativa'),
        ('off', 'Inativa'),
    )

    nomeEmpresa = models.CharField(max_length=96)
    nomeAmigavel = models.CharField(max_length=96)
    cnpj = models.CharField(max_length=24)
    endereco = models.CharField(max_length=96)
    numeroEmpresa = models.CharField(max_length=24)
    cidade = models.CharField(max_length=96)
    estado = models.CharField(max_length=96)
    telefone = models.CharField(max_length=24, blank = True, null = True)
    whatsapp = models.CharField(max_length=24)
    email = models.EmailField()
    facebook = models.CharField(max_length=96, blank = True, null = True)
    instagram = models.CharField(max_length=96, blank = True, null = True)
    canalYoutube = models.CharField(max_length=96, blank = True, null = True)
    analytics = models.CharField(max_length=96, blank = True, null = True)
    ramoAtividade = models.TextField()
    tituloPagina = models.CharField(max_length=96)
    descricaoPagina = models.CharField(max_length=96)
    logotipo = models.TextField()
    scriptHeader = models.TextField()
    scriptBody = models.TextField()
    scriptFooter = models.TextField()
    status = models.CharField(
        max_length=7,
        choices=STATUS,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomeEmpresa


  
