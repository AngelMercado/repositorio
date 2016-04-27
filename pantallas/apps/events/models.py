from django.db import models

# Create your models here.
class Event(models.Model):

	title = models.CharField(max_length = 180 , null= True, blank = True)
	pub_date=models.DateField(auto_now=False, auto_now_add=False)
	description = models.TextField(max_length = 1000 , null= True, blank = True)
	img = models.FileField(upload_to='Events/', null=True, blank =True)

	def __str__(self):
		return self.title + "( " + str(self.pub_date)+" )"