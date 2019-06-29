from django.forms import ModelForm, Textarea
from .models import Tipo, Produtos

class TipoForm(ModelForm):
	class Meta:
		model = Tipo
		fields = ['tipo']
class ProdutosForm(ModelForm):
	class Meta:
		model = Produtos
		fields = ['nome', 'preco', 'descricao', 'quantidade', 'imagem', 'tipo']
		widgets = {
            'descricao': Textarea(),
        }