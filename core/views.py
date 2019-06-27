from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')
def listaprodutos(request):
	return render(request, 'listaprodutos.html')
def login(request):
	return render(request, 'login.html')
def cadastro(request):
	return render(request, 'cadastro.html')
def perfil(request):
	return render(request, 'perfil.html')
def tipos(request):
	return render(request, 'tipos.html')
def cadastrartipo(request):
	return render(request, 'cadastrartipo.html')
def produtos(request):
	return render(request, 'produtos.html')
def produto(request):
	return render(request, 'produto.html')
def produtoespecifico(request, id):
	return render(request, 'nomeproduto.html')
