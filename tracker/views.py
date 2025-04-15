import csv
import io
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm
from datetime import datetime
from django.shortcuts import redirect, get_object_or_404
from .models import Transaction

def home(request):
    return render(request, 'home.html')  # Ensure this template exists

def tracker_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction added successfully!")
            return redirect('tracker')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all().order_by('-date')

    current_year = datetime.now().year
    years = range(2020, current_year + 2)

    context = {
        'form': form,
        'transactions': transactions,
        'months': range(1, 13),
        'years': years,
    }
    return render(request, 'tracker.html', context)

def delete_transaction(request, pk):
    if request.method == "POST":
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
    return redirect('tracker')

def export_csv(request):
    month = request.GET.get('month')
    year = request.GET.get('year')

    if not month or not year:
        messages.error(request, "Month and Year are required to export transactions.")
        return redirect('tracker')

    transactions = Transaction.objects.filter(date__year=year, date__month=month)

    if not transactions.exists():
        messages.warning(request, "No transactions found for the selected month and year.")
        return redirect('tracker')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="transactions_{month}_{year}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Description', 'Category', 'Amount'])

    for t in transactions:
        writer.writerow([t.date, t.description, t.category, t.amount])

    return response

def import_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        try:
            csv_file = request.FILES['csv_file'].read().decode('utf-8')
            reader = csv.reader(io.StringIO(csv_file))
            next(reader)  # Skip header row
            created_count = 0

            for row in reader:
                if len(row) != 4:
                    continue  # Skip malformed rows
                date, description, category, amount = row
                Transaction.objects.create(
                    date=date,
                    description=description,
                    category=category,
                    amount=amount
                )
                created_count += 1

            messages.success(request, f"Successfully imported {created_count} transaction(s).")
        except Exception as e:
            messages.error(request, f"Failed to import transactions: {str(e)}")

        return redirect('tracker')

    return HttpResponse("Invalid request", status=405)
