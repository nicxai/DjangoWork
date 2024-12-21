from django.shortcuts import render
from main.models import *

# Create your views here.
def main(requests):
    main = Main.objects.latest('id')
    return render(requests, 'index.html', locals())

def benner(requests):
    benner = Benner.objects.latest('id')
    return render(requests, 'benner.html', locals())