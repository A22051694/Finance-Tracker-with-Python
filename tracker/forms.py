from django import forms
from .models import Transaction

CATEGORY_CHOICES = [
    ('income', 'Income'),
    ('groceries', 'Groceries'),
    ('rent', 'Rent'),
    ('entertainment', 'Entertainment'),
    ('others', 'Others'),
    ('custom', 'Custom'),
]

class TransactionForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    custom_category = forms.CharField(max_length=100, required=False, label='Custom Category')

    class Meta:
        model = Transaction
        fields = ['date', 'description', 'category', 'custom_category', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        custom_category = cleaned_data.get('custom_category')

        if category == 'custom':
            if not custom_category:
                self.add_error('custom_category', 'Please enter a custom category.')
            else:
                cleaned_data['category'] = custom_category  # Override
        return cleaned_data
