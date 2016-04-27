from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Teacher
# Create your views here.
class IndexAcademics(TemplateView):
	template_name = 'academicos.html'

	def get_context_data(self,**kwargs):
		context = super(IndexAcademics,self).get_context_data(**kwargs)
		teachers = Teacher.objects.all()
		objects = Teacher.objects.count()		
		context['teachers'] = teachers


		
		return context

