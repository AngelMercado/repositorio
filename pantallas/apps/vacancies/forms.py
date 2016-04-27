from django import forms
from .models import Vacancy

class FilterVacancies(forms.Form):
	rango= (
		('Informatica','Informatica'),
		('Mecatronica','Mecatronica'),
		('Industrial','Industrial'),
		('Biotecnologia','Biotecnologia'),
		('MECA','Mecanica Automotriz'),
		('Energia','Energia'),
		('Negocios_Internacionales','Negocios Internacionales'),		
	)

	

	filtro = forms.ChoiceField(required=False,
        widget=forms.Select, choices=rango)

	def process(self):
	   
	    cd = self.cleaned_data

	
