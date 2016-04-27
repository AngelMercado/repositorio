from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView,ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Vacancy
from .forms import FilterVacancies

# Create your views here.

class VacancyIndex(FormView):
	template_name = 'bolsa.html'
	form_class = FilterVacancies
	success_url='/Vacantes'
	filtro= 'Informatica'
	context_object_name='vacancies'

	def post(self, request, *args, **kwargs):
		form = FilterVacancies(request.POST)
		if form.is_valid():
			self.filtro = form.cleaned_data['filtro']
			print self.filtro
			vacancies_list = Vacancy.objects.filter(career = self.filtro).order_by('-pubDate')
			vacancies = vacancies_list

		return render(request, self.template_name, {'form': form, 'vacancies':vacancies})


        


		
		
		

	


	


	
	

		

	
