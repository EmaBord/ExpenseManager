from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from expense.models import Expense

class ExpenseCreate(CreateView):
    model = Expense
    fields = ['descripcion','precio']  
    def get_success_url(self):
        return reverse('expense-list')		
class ExpenseUpdate(UpdateView):
    model = Expense
    template_name_suffix = '_update_form'
    fields = ['descripcion','precio']	  
    def get_success_url(self):
        return reverse('expense-list')    
class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense-list')

class ExpenseListView(ListView):

    model = Expense

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        total = 0
        expenses = Expense.objects.all()
        for e in expenses:
            total = total + e.precio
        context['total'] = total    
        return context
