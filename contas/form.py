from django.forms import ModelForm
from .models import Transacao, Cliente

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'observacoes', 'categoria']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'bairro', 'endereco']