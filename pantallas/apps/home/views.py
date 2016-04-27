from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Slide
# homes views
class IndexView(TemplateView):
	template_name = 'index.html'
	def get_context_data(self,**kwargs):
		context = super(IndexView,self).get_context_data(**kwargs)
		slides = Slide.objects.all()
		context['slides'] = slides
		return context
	


def send_email(request):
	username = 'Angel Enrique'
	#msg llamamos a un constructor
	msg = EmailMessage(subject='Bienvenido',
		from_email='Sistema UPVT <myjava@outlook.es>',
		to = ['dragon_firer@hotmail.com'])
	#template de mailchimp
	msg.template_name = 'welcome'
	#llenar contenido dinamico del template buscar identificador en mailchimp
	msg.template_content = {
		'std_content00' : 'Hola %s Bienvenido' % username
	}
	msg.send()


