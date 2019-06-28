"""info419info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, listaprodutos, produtoespecifico, cadastro, perfil, editarperfil, tipos, editartipo, apagartipo, cadastrartipo, produtos, editarprodutos, apagarprodutos, produto
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('produtos/', listaprodutos, name="listaprodutos"),
    path('produtos/<int:id>/', produtoespecifico, name="produtoespecifico"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('cadastrar/', cadastro, name="cadastro"),
    path('perfil/', perfil, name="perfil"),
    path('perfil/editar/<int:id>', editarperfil, name="editarperfil"),
    path('perfil/tipos/', tipos, name="tipos"),
    path('perfil/tipos/editar/<int:id>/', editartipo, name="editartipo"),
    path('perfil/tipos/apagar/<int:id>/', apagartipo, name="apagartipo"),
    path('perfil/tipos/cadastrar', cadastrartipo, name="cadastrartipo"),
    path('perfil/produtos', produtos, name="produtos"),
    path('perfil/produtos/editar/<int:id>/', editarprodutos, name="editarprodutos"),
    path('perfilprodutos/apagar/<int:id>/', apagarprodutos, name="apagarprodutos"),
    path('perfil/produtos/cadastrar', produto, name="produto"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)