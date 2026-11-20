import json
from datetime import date

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ExpenseForm
from .models import Expense

# Display settings for each category (name -> icon, colour)
CATEGORY_META = {
    'Food':     {'icon': 'bi-basket2-fill',      'color': '#f59e0b'},
    'Travel':   {'icon': 'bi-airplane-fill',     'color': '#3b82f6'},
    'Shopping': {'icon': 'bi-bag-fill',          'color': '#ec4899'},
    'Bills':    {'icon': 'bi-receipt',           'color': '#10b981'},
}


def dashboard(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.order_by('-date', '-id')

    total = expenses.aggregate(t=Sum('amount'))['t'] or 0
    total_records = expenses.count()

    today = date.today()
    month_total = expenses.filter(
        date__year=today.year, date__month=today.month
    ).aggregate(t=Sum('amount'))['t'] or 0

    sums = {
        row['category']: row['t']
        for row in expenses.values('category').annotate(t=Sum('amount'))
    }

    categories = []
    for name, meta in CATEGORY_META.items():
        amount = sums.get(name, 0) or 0
        categories.append({
            'name': name,
            'icon': meta['icon'],
            'color': meta['color'],
            'total': amount,
            'percent': round(amount / total * 100) if total else 0,
        })

    top_category = max(categories, key=lambda c: c['total']) if total else None

    context = {
        'form': form,
        'expenses': expenses,
        'total': total,
        'total_records': total_records,
        'month_total': month_total,
        'today': today,
        'categories': categories,
        'top_category': top_category,
        'category_meta': CATEGORY_META,
        'chart_data': {
            'labels': [c['name'] for c in categories],
            'values': [c['total'] for c in categories],
            'colors': [c['color'] for c in categories],
        },
    }

    return render(request, 'dashboard.html', context)


@require_POST
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('dashboard')