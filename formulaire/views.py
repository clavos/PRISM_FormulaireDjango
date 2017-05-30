#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render

def formulaire(request):
    return render(request, 'formulaire/index.html', {'date': datetime.now()})