from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student
# Create your views here.
class IndexCareer(TemplateView):
	template_name = 'carrera.html'

	def get_context_data(self,**kwargs):
		context = super(IndexCareer,self).get_context_data(**kwargs)
		students = Student.objects.all()
		context['students'] = students
		return context

