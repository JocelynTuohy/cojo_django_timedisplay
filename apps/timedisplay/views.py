# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render #, HttpResponse

# Create your views here.
def index(request):
    print '$'*50
    now = datetime.today()
    context = {
        "date": now.strftime('%b %d, %Y'),
        "time": now.strftime('%I:%M %p')
    }
    return render(request, 'timedisplay/index.html', context)
