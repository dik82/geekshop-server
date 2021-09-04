from django.shortcuts import render

import os
import json

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.
# Контроллер-функция
def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'index.html', context)


def products(request):
    context = {'title': 'Каталог'}
    path_file = os.path.join(MODULE_DIR, 'fixtures/myfiles.json')
    context['products'] = json.load(open(path_file, encoding='utf-8'))
    return render(request, 'products.html', context)
