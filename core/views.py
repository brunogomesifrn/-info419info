from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, 'login.html')
def index(request):
	pass
def cadastrar(request):
	return render(request, 'cadastro.html')