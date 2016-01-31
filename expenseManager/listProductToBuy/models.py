
from django.db import models

# Create your models here.

class ProductToBuy(models.Model):	
	nombre 	= models.CharField(max_length =100)
	class Meta:
		ordering = ['-id']
	