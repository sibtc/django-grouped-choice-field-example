from django import forms

from .fields import GroupedModelChoiceField
from .models import Category, Expense


class ExpenseForm(forms.Form):
    CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )
    amount = forms.DecimalField()
    date = forms.DateField()
    category = forms.ChoiceField(choices=CHOICES)


class GroupedExpenseForm(forms.Form):
    CHOICES = (
        ('Debt', (
            (11, 'Credit Card'),
            (12, 'Student Loans'),
            (13, 'Taxes'),
        )),
        ('Entertainment', (
            (21, 'Books'),
            (22, 'Games'),
        )),
        ('Everyday', (
            (31, 'Groceries'),
            (32, 'Restaurants'),
        )),
    )
    amount = forms.DecimalField()
    date = forms.DateField()
    category = forms.ChoiceField(choices=CHOICES)


class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'date', 'category')


class GroupedExpenseModelForm(forms.ModelForm):
    category = GroupedModelChoiceField(queryset=Category.objects.exclude(parent=None), choices_groupby='parent')

    class Meta:
        model = Expense
        fields = ('amount', 'date', 'category')
