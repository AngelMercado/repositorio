from django.db import models

# Create your models here.
class Slide(models.Model):
	name = models.CharField(max_length = 100, null=True, blank=True)
	description = models.TextField(max_length =300, null=True, blank=True)
	docfile = models.FileField(upload_to='slides/%Y/%m/%d', null = True)
	link = models.URLField(max_length='200', null=True,blank=True)

	def __str__(self):
		return " slide "+str(self.id)+" "+self.name
