from django.shortcuts import render, redirect
from django.views.generic import TemplateView,FormView
from .forms import GripBoxForm
from .models import GripBox
from django.core.mail import EmailMessage
# Create your views here.
class GripBoxIndex(FormView):
	template_name= 'buzon.html'
	form_class = GripBoxForm
	success_url = '/buzon'

	def post(self,request, *args,**kwargs):
		send_email(request)
		return redirect('/')

	def form_valid(self,form):
		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		comentario = form.cleaned_data['comentario']
		new = GripBox(nombre = name,email = email,comentario = comentario)
		new.save()

		return super(GripBoxIndex,self).form_valid(form)

	def form_invalid(self, form):
		print 'fallo'
		return super(GripBoxIndex,self).form_invalid(form)


def send_email(request):
	username = 'Angel Enrique'
	#msg llamamos a un constructor
	msg = EmailMessage(subject='Bienvenido',from_email = 'angelmercado930@gmail.com',to =['dragon_firer@hotmail.com'])
	msg.template_name = 'welcome'
	msg.template_content = {
	'std_content00' : 'Bienvenido',
	}
	msg.send()
