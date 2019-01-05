from django.db import models

# Create your models here.
class Group(models.Model):
	"""docstring for Group"""
	first_name = models.CharField(max_length=50)
	
		