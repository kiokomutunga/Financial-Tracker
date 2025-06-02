from django.shortcuts import render , redirect
from .models import Transactions
from .forms import TransactionForm


def Dashboard (request):
    transactions = Transactions.objects.all().order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expenses')
    balance  = total_income - total_expense


    return render (request, 'tracker/dashboard.html',{
            'transactions':transactions,
            'total_income':total_income,
            'total_expense':total_expense,
            'balance': balance

        }
    )

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_Valid():
            form.save()
            return redirect('dashboard')
        else:
            form = TransactionForm()
            return render(request, 'tracker/add_transaction.html', {'form': form})
        
      

