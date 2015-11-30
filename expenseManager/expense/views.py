from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from expense.models import Expense

from django.views.generic.dates import MonthArchiveView

from django.shortcuts import render
class ExpenseMonthArchiveView(MonthArchiveView):
    queryset = Expense.objects.all()
    date_field = "fecha"
    allow_future = True
    template_name = 'expense/expense_archive_month.html'
    def get_context_data(self, **kwargs):
        context = super(ExpenseMonthArchiveView, self).get_context_data(**kwargs)
        total = 0
        expenses = Expense.objects.all()
        for e in expenses:
            total = total + e.precio
        context['total'] = total    
        return context
    def get(self, request, *args, **kwargs):
        
        expenses = Expense.objects.filter(fecha__year=kwargs['year'],fecha__month=kwargs['month'])
        total = 0
        for e in expenses:
            total = total + e.precio
        
        return render(request,self.template_name,{'object_list':expenses,'total':total})    


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
        import datetime
        ahora = datetime.datetime.now()
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        total = 0
        expenses = Expense.objects.filter(fecha__year=ahora.year,fecha__month=ahora.month)
        for e in expenses:
            total = total + e.precio
        context['total'] = total    
        context['object_list'] = expenses
        return context
   

