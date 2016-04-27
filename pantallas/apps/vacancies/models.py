from django.db import models
from django.utils.encoding import smart_text

# Create your models here.
class Vacancy(models.Model):
	Informatica = 'Informatica'
   	Mecatronica = 'Mecatronica'
   	Industrial = 'Industrial'
   	Biotecnologia = 'Biotecnologia'
   	Mecanica_Automotriz = 'Mecanica_Automotriz'
   	Energia = 'Energia'
   	Negocios_Internacionales = 'Negocios_Internacionales'

	CAREER_CHOICES = (
	(Informatica,'Informatica'),
	(Mecatronica,'Mecatronica'),
	(Industrial,'Industrial'),
	(Biotecnologia,'Biotecnologia'),
	(Mecanica_Automotriz,'Mecanica_Automotriz'),
	(Energia,'Energia'),
	(Negocios_Internacionales,'Negocios_Internacionales'),
	)
	career = models.CharField(max_length=60,blank=True,null=True,choices=CAREER_CHOICES)
	company = models.CharField(max_length=120,blank=True,null=True)
	pubDate = models.DateField(auto_now=False, auto_now_add=False)
	description = models.TextField(max_length=360,blank=True,null=True)
	pdf = models.FileField(upload_to='Vacancies/', null = True, blank = True)

	def __str__(self):
		return self.career+" "+self.company+" "+str(self.pubDate)
