from django import forms

from .models import Mensages

class MensageForm(forms.ModelForm):
	
	class Meta:
		model = Mensages
		fields = ("email", "assunto", "mensagem")