from django import forms
from .models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['Type', 'category', 'amount', 'description']