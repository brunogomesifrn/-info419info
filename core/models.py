from django.db import models
# Create your models here.

class Tipo (model.Model):
		tipo = models.CharField('tipo')

class Produtos (model.Model):
		produto = models.CharField('produtos', max_length=100)
		nome = models.CharField('nome', max_length=100)
		preco = models.FloatField('preco', max_length=100)
		descricao = models.CharField('descricao', max_length=100)
		quantidade = models.IntergeField('quantidade', max_length=100)
		imagem = models.ImageField('imagem', upload_to='img')
		tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
