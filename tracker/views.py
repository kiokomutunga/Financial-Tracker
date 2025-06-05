from django.shortcuts import render, redirect
from .models import Transactions, Budget
from .forms import TransactionForm
from collections import defaultdict
from datetime import datetime
import json

def Dashboard(request):
    # Get current datetime
    now = datetime.now()

    # Define start and end of the current month
    start_of_month = datetime(now.year, now.month, 1)
    if now.month == 12:
        end_of_month = datetime(now.year + 1, 1, 1)
    else:
        end_of_month = datetime(now.year, now.month + 1, 1)

    # Filter transactions and budgets for current month
    transactions = Transactions.objects.filter(date__gte=start_of_month, date__lt=end_of_month).order_by('-date')
    budgets = Budget.objects.filter(date__gte=start_of_month, date__lt=end_of_month)

    # Compute totals
    total_income = sum(t.amount for t in transactions if t.Type == 'income')
    total_expense = sum(t.amount for t in transactions if t.Type == 'expenses')
    balance = total_income - total_expense

    income_expense_data = [total_income, total_expense]

    # Prepare chart data
    category_totals = defaultdict(float)
    for t in transactions:
        category_totals[t.category] += t.amount

    chart_labels = list(category_totals.keys())
    chart_data = list(category_totals.values())

    # Budget warnings (Optional logic, you can enhance this)
    budget_warnings = []

    return render(request, 'tracker/dashboard.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
        'budgets': budgets,
        'budget_warnings': budget_warnings,
        'income_expense_data':income_expense_data,
    })

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})
