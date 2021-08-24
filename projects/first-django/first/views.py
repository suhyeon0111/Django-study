from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime
import random
# Create your views here.


def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)
    #사용자가 요청하면 helloworld를 돌려주고 싶은 거임


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number'])

    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1) 

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results
    }
    return render(request, 'first/result.html', context)
