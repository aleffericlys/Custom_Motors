from distutils.command import upload
from json import load
from logging.config import valid_ident
from telnetlib import STATUS
from venv import create
from django.db import models
from django.shortcuts import get_object_or_404
from matplotlib.pyplot import title


class Motos(models.Model):

	nome = models.CharField(max_length=255)
	modelo = models.CharField(max_length=255)
	fabricante = models.CharField(max_length=255)
	valor = models.FloatField()
	motor = models.FloatField()
	quantidade = models.IntegerField()
	imagen = models.ImageField(upload_to = 'media')
	description = models.TextField()

	def __str__(self):
		return self.nome


class Acessorios(models.Model):

	nome = models.CharField(max_length=255)
	tipo = models.CharField(max_length=255)
	marca = models.CharField(max_length=255)
	valor = models.FloatField()
	quantidade = models.IntegerField()
	imagen = models.ImageField(upload_to = 'media')
	description = models.TextField()

	def __str__(self):
		return self.nome

class Ferramentas(models.Model):

	nome = models.CharField(max_length=255)
	tipo = models.CharField(max_length=255)
	marca = models.CharField(max_length=255)
	valor = models.FloatField()
	quantidade = models.IntegerField()
	imagen = models.ImageField(upload_to = 'media')
	description = models.TextField()

	def __str__(self):
		return self.nome


class Mensages(models.Model):
	escolhas = (
		("comentario", "Comentários"),
		("critica", "Críticas"),
		("duvida", "Dúvidas"),
		("outro", "Outros"),
	)

	email = models.EmailField()
	assunto = models.CharField(
		max_length=10,
		choices=escolhas,
	)
	mensagem = models.TextField()
	data = models.DateTimeField(auto_now_add=True)
	# user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		return str(self.email)
# Create your models here.

