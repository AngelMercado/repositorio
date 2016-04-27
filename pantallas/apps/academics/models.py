from django.db import models
# Create your models here.
class Teacher(models.Model):
	fullName = models.CharField(max_length = 150 , null= True, blank = True)
	position = models.CharField(max_length = 30 , null= True, blank = True)
	academy =models.CharField(max_length = 150 , null= True, blank = True)
	pdf = models.FileField(upload_to='Teacher/horario/', null = True, blank = True)
	img = models.FileField(upload_to='Teavher/img/', null=True, blank =True)
	def __str__(self):
		return self.fullName


