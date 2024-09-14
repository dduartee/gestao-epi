from django import forms

from gestaoepi import settings
from .models import Colaborador, EPIGenerico, Produto

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'telefone', 'cargo']  # Inclua todos os campos que você deseja no formulário

        # Opcionalmente, você pode personalizar os labels dos campos
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'cargo': 'Cargo',
        }
        opcoesCargo = {
            "Mestre de obras": "Mestre de obras",
            "Pedreiro": "Pedreiro",
            "Servente": "Servente",
        }
        
        # Definindo widgets para personalizar os inputs no HTML
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}, choices=opcoesCargo),
        }
class EPIForm(forms.ModelForm):
    class Meta:
        model = EPIGenerico
        fields = ['nome', 'descricao', 'prazo_dias']        
        nome = forms.CharField(label='Nome', max_length=100)
        descricao = forms.CharField(label='Descrição', max_length=100)
        prazo_dias = forms.IntegerField(label='Prazo de uso (dias)')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do EPI'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição do EPI'}),
            'prazo_dias': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o prazo de uso em dias'}),
        }
        
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['epi_generico', 'qtd_estoque', 'numero_ca', 'data_validade_ca']
        epi_generico = forms.ModelChoiceField(queryset=EPIGenerico.objects.all())
        qtde_estoque = forms.IntegerField(label='Quantidade em estoque')
        numero_ca = forms.CharField(label='Número do CA', max_length=100)
        data_validade_ca = forms.DateField(label='Data de validade do CA', input_formats=settings.DATE_INPUT_FORMATS);
        
        
        
        