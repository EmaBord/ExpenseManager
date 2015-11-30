from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
# Create your models here.

class Expense(models.Model):
	fecha 			= models.DateField(default=timezone.now)
	descripcion 	= models.CharField(max_length =100)
	precio			= models.FloatField() 
	extraordinario	= models.IntegerField(choices = ((1, ("Si")),(0, ("No"))),default=0)
	def get_absolute_url(self):
		return reverse('expense-detail', kwargs={'pk': self.pk})	
