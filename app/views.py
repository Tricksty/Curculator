import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def function_1(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        # казалось бы это должно работать так
        amount_at_start = float(data['amount_at_start'])
        deposit_percent = float(data['deposit_percent'])
        ages = float(data['ages'])
        inflation_rate = 4.5
        amount_at_end = (amount_at_start * (1 + deposit_percent / 100) ^ ages) / (1 + inflation_rate / 100) ^ ages
        result = {
            'amount_at_end': amount_at_end,
        }
    return result
