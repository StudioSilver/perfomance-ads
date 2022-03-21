from django import forms

from .models import Empresa

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ('nomeEmpresa', 'cnpj', 'nomeAmigavel', 'endereco', 'numeroEmpresa', 'cidade',
                    'estado', 'telefone', 'whatsapp', 'email', 'facebook', 'instagram', 'canalYoutube',
                    'analytics', 'ramoAtividade', 'tituloPagina', 'descricaoPagina')