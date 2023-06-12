from django.shortcuts import render, HttpResponse

import datetime

# Create your views here.

def index(request):
    tasks = range(20)
    date = datetime.date.today()
    return render(request, 'app/index.html', {
        'tasks': tasks,
        'date': date
    })