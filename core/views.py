from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, 'login.html')
def index(request):
	return render(request, 'index.html')
def cadastro(request):
	pass
	pass
def cadastrar(request):
	return render(request, 'cadastro.html')
