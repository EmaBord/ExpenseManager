from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from listProductToBuy.models import ProductToBuy
from django.shortcuts import render



class ProductToBuyCreate(CreateView):
    model = ProductToBuy
    fields = ['nombre']  
    #template_name = "listProductToBuy/producttobuy_list.html"
    def get_success_url(self):
        return reverse('ProductToBuy-list')		

class ProductToBuyUpdate(UpdateView):
    model = ProductToBuy
    template_name = "listProductToBuy/producttobuy_update.html"
    fields = ['nombre']	  
    def get_success_url(self):
        return reverse('ProductToBuy-list')    

class ProductToBuyDelete(DeleteView):
    model = ProductToBuy
    template_name = "listProductToBuy/producttobuy_list.html"
    success_url = reverse_lazy('ProductToBuy-list')

class ProductToBuyListView(ListView):
	template_name = "listProductToBuy/producttobuy_list.html"
	model = ProductToBuy
    
   

