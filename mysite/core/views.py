from django.shortcuts import render

from .forms import ExpenseForm, GroupedExpenseForm, ExpenseModelForm, GroupedExpenseModelForm


def home(request):
    # Forms
    expense_form = ExpenseForm()
    grouped_expense_form = GroupedExpenseForm()

    # Model Forms
    expense_model_form = ExpenseModelForm()
    grouped_expense_model_form = GroupedExpenseModelForm()

    return render(request, 'home.html', {
        'expense_form': expense_form,
        'grouped_expense_form': grouped_expense_form,
        'expense_model_form': expense_model_form,
        'grouped_expense_model_form': grouped_expense_model_form,
    })
