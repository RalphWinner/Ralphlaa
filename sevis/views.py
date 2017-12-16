from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def porno(request):
	return(render(request, 'sevis/porno.html'))

def serie(request):
	return(render(request, 'sevis/serie.html'))

def film(request):
	return(render(request, 'sevis/film.html'))