from django.db import models

# Create your models here.
class GripBox(models.Model):
	nombre = models.CharField(max_length= 100,null= True,blank=True)
	email = models.CharField(max_length= 100,null= True,blank=True)
	comentario = models.TextField(max_length= 500,null= True,blank=True)


