from django import forms
from .models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['Type', 'amount', 'description', 'category']
        widgets = {
            'Type': forms.Select(attrs={'id': 'id_type'}),
            'category': forms.Select(attrs={'id': 'id_category'}),
        }