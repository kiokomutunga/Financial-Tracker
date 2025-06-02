from django.shortcuts import render , redirect
from .models import Transactions
from .forms import TransactionForm
from collections import defaultdict
import json


def Dashboard (request):
    transactions = Transactions.objects.all().order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expenses')
    balance  = total_income - total_expense

    #charts data
    category_totals = defaultdict(float)
    for t in transactions:
        category_totals[t.category] += t.amount

    chart_labels = list(category_totals.keys())
    chart_data = list(category_totals.values())


    return render (request, 'tracker/dashboard.html',{
            'transactions':transactions,
            'total_income':total_income,
            'total_expense':total_expense,
            'balance': balance,
            'chart_labels': json.dumps(chart_labels) ,
            'chart_data': json.dumps(chart_data),

        }
    )

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('dashboard')
        else:
            form = TransactionForm()
            return render(request, 'tracker/add_transaction.html', {'form': form})
        
      

