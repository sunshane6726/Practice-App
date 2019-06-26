from django.shortcuts import render
from .models import Portpolio



def portfolio(request):
    portfolios = Portpolio.objects   
    return render(request, 'portfolio/portpolio.html', {'portfolios':portfolios})