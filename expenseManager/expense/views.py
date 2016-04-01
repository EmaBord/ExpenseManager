from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from expense.models import Expense
from django.views.generic.dates import MonthArchiveView
from django.shortcuts import render
from pytz import timezone 
buenos_aires = timezone('America/Argentina/Buenos_Aires')
class TemplateMethod():
    def context(self,year,month):
        context = {}
        total = 0
        extraordinario = 0
        expenses = Expense.objects.filter(fecha__year=year,fecha__month=month)
        context['object_list'] = expenses
        for e in expenses:
            total = total + e.precio
            if e.extraordinario:
                extraordinario+=e.precio
        context['extraordinario'] = extraordinario        
        context['total'] = total   
        return context


class ExpenseMonthArchiveView(MonthArchiveView,TemplateMethod):
    queryset = Expense.objects.all()
    date_field = "fecha"
    allow_future = True
    template_name = 'expense/expense_list.html'
    def get(self, request, *args, **kwargs):        
        return render(request,self.template_name,self.context(kwargs['year'],kwargs['month']))    

class ExpenseCreate(CreateView):
    model = Expense
    fields = ['descripcion','precio','extraordinario']  
    def get_success_url(self):
        return reverse('expense-list')		

class ExpenseUpdate(UpdateView):
    model = Expense
    template_name_suffix = '_update_form'
    fields = ['descripcion','precio','extraordinario']	  
    def get_success_url(self):
        return reverse('expense-list')    

class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense-list')

class ExpenseListView(ListView,TemplateMethod):
    model = Expense
    def get_context_data(self, **kwargs):
        import datetime
        ahora = datetime.datetime.now(buenos_aires).replace(tzinfo=None)
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        context.update(self.context(ahora.year,ahora.month))  
        return context
   

