from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests, 'receitas/home.html')