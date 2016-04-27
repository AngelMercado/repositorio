from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 100, null=True, blank=True)
	comment = models.CharField(max_length = 100, null=True, blank=True)
	career = models.CharField(max_length = 100, null=True, blank=True)
	img = models.FileField(upload_to='students/img/%Y/%m/%d', null = True)

	def __str__(self):
		return self.name+" "+self.career
