from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
# Create your models here.
from pytz import timezone 
from datetime import datetime
buenos_aires = timezone('America/Argentina/Buenos_Aires')
class Expense(models.Model):
	fecha 			= models.DateField(default=datetime.now(buenos_aires).replace(tzinfo=None))
	descripcion 	= models.CharField(max_length =100)
	precio			= models.FloatField() 
	extraordinario	= models.IntegerField(choices = ((1, ("Si")),(0, ("No"))),default=0)
	class Meta:
		ordering = ['-id']
	def get_absolute_url(self):
		return reverse('expense-detail', kwargs={'pk': self.pk})	
