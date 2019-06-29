from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tipo, Produtos
from .forms import TipoForm, ProdutosForm

# Create your views here.
def index(request):
	produtos = Produtos.objects.all().order_by('-id')[:3]
	contexto = {
	'produto': produtos
	}
	return render(request, 'index.html', contexto)
def listaprodutos(request):
	return render(request, 'listaprodutos.html')
def login(request):
	return render(request, 'login.html')
def cadastro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro.html', contexto)
@login_required
def perfil(request):
	usuario = User.objects.all().order_by('-id')[:1]
	contexto = {
	'usuario': usuario
	}
	return render(request, 'perfil.html')
@login_required
def editarperfil(request,id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
	'form': form
	}
	return render(request, 'cadastro.html', contexto)
@login_required
def tipos(request):
	tipo = Tipo.objects.all()
	contexto = {
	'tipo': tipo
	}
	return render(request, 'tipos.html', contexto)
@login_required
def cadastrartipo(request):
	form = TipoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/perfil/tipos')
	contexto = {
	'form': form
	}
	return render(request, 'cadastrartipo.html', contexto)
@login_required
def editartipo(request, id):
	tipo = Tipo.objects.get(pk=id)
	form = TipoForm(request.POST or None, instance=tipo)
	if form.is_valid():
		form.save()
		return redirect('/perfil/tipos')
	contexto = {
	'form': form
	}
	return render(request, 'cadastrartipo.html', contexto)
@login_required
def apagartipo(request, id):
	tipo = Tipo.objects.get(pk=id)
	tipo.delete()
	return redirect('/perfil/tipos')
@login_required
def produtos(request):
	produtos = Produtos.objects.all()
	contexto = {
	'produto': produtos
	}
	return render(request, 'produtos.html', contexto)
@login_required
def editarprodutos(request, id):
	produtos = Produtos.objects.get(pk=id)
	form = ProdutosForm(request.POST or None, request.FILES or None, instance=produtos)
	if form.is_valid():
		form.save()
		return redirect('/perfil/produtos')
	contexto = {
	'form': form
	}
	return render(request, 'produto.html', contexto)
@login_required
def apagarprodutos(request, id):
	produtos = Produtos.objects.get(pk=id)
	produtos.delete()
	return redirect('/perfil/produtos')
@login_required
def produto(request):
	form = ProdutosForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('/perfil/produtos')
	contexto = {
	'form': form
	}
	return render(request, 'produto.html', contexto)
@login_required
def produtoespecifico(request, id):
	produtos = Produtos.objects.get(pk=id)
	contexto = {
	'produto': produtos
	}
	return render(request, 'nomeproduto.html', contexto)
