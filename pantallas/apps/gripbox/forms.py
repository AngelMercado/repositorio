from django import forms

class GripBoxForm(forms.Form):
	name = forms.CharField(max_length=100,
		widget=forms.TextInput(attrs ={
				'type':'text',
				'name':'name',
				'class':'form-control name-field',
				'placeholder':'Tu nombre',
				'required':'required'


			}))
	email = forms.CharField(max_length=100,
		widget=forms.TextInput(attrs ={
				'type':'email',
				'name':'email',
				'class':'form-control mail-field',
				'placeholder':'Tu email',
				'required':'required'


			}))
	comentario = forms.CharField(max_length=50,
		widget=forms.Textarea(attrs ={
				'type':'text',
				'name':'comentario',
				'class':'form-control',
				'rows':'8',
				'placeholder':'Comentario',
				'required':'required'


			}))
	