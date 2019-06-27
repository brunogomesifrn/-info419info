from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, 'login.html')
def index(request):
	return render(request, 'index.html')
def cadastro(request):
	return render(request, 'cadastro.html')
def cadastrartipo(request):
	return render(request, 'cadastrartipo.html')
