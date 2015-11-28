from django import forms
from expenseManager.expense.models import *

class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense

