from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(requests):
    return HttpResponse('Home') 

def contato(requests):
    return HttpResponse('Contato') 

def sobre(requests):
    return HttpResponse('Sobre') 