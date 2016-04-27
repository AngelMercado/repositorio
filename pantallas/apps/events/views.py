from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event
# Create your views here.

class EventIndex(TemplateView):
	template_name = 'eventos.html'

	def get_context_data(self,**kwargs):
		context = super(EventIndex,self).get_context_data(**kwargs)
		event_list = Event.objects.all()
		paginator = Paginator(event_list,6)
		page = self.request.GET.get('page')
		try:
			events = paginator.page(page)
		except PageNotAnInteger:
			# if is not a integer, deliver firts page
			events = paginator.page(1)
		except EmptyPage:
			#if is out of rage, deliver the last page
			events = paginator.page(paginator.num_pages)

		context['events'] = events

		return context