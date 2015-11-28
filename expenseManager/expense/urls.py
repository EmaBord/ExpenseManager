from django.conf.urls import patterns, url
from expense.views import *
urlpatterns = patterns ('expenseManager.expense.views',
			 url(r'expense/add/$', ExpenseCreate.as_view(), name='expense-add'),
			 url(r'expense/(?P<pk>[0-9]+)/$', ExpenseUpdate.as_view(), name='expense-update'),
    			 url(r'expense/(?P<pk>[0-9]+)/delete/$', ExpenseDelete.as_view(),  name='expense-delete'),
			 url(r'^$', ExpenseListView.as_view(), name='expense-list'),
			  url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',ExpenseMonthArchiveView.as_view(month_format='%m'),name="expense_month_filter"),
			)
