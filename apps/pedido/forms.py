from django import forms
from .models import *


class ProvinciaForm(forms.ModelForm):
	class Meta:
		model = Provincia
		fields = '__all__'

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields = '__all__'

class ComunaForm(forms.ModelForm):
	class Meta:
		model = Comuna
		fields = '__all__'

class PagoForm(forms.ModelForm):
	class Meta:
		model = Pago
		exclude = ['projecto_legalizado']

class TerrenoLegalizarForm(forms.ModelForm):
	class Meta:
		model = TerrenoLegalizar
		# exclude = ['pessoaEmpresa','user']
		fields = ['projecto','localizacao','provincia_arquivacao','quarterao','municipio','comuna', 'metros','pago_apreciado']

class PessoaEmpresaForm(forms.ModelForm):
	class Meta:
		model = PessoaEmpresa
		fields = '__all__'

class DirectivoForm(forms.ModelForm):
	class Meta:
		model = Directivo
		fields = '__all__'