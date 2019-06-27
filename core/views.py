from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'index.html')
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
	return render(request, 'tipos.html')
@login_required
def cadastrartipo(request):
	return render(request, 'cadastrartipo.html')
@login_required
def produtos(request):
	return render(request, 'produtos.html')
@login_required
def produto(request):
	return render(request, 'produto.html')
@login_required
def produtoespecifico(request, id):
	return render(request, 'nomeproduto.html')
