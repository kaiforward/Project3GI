# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Element
from companies.models import CompanyStorage
from django.shortcuts import redirect
from companies.views import company_trade, planet_trade
from planets.models import PlanetType, Planet, PlanetStorage
from django.db.models import Count, Avg

@login_required(login_url='/login/')
def element_view(request):
	elements = Element.objects.all()
	# planet_averages = PlanetStorage.objects.values('element').annotate(avg_price=Avg('price'))
	# company_averages = CompanyStorage.objects.values('element').annotate(avg_price=Avg('price'))
	return render(request, "elements.html", {'elements': elements}) 

@login_required(login_url='/login/')
def filter_element(request, element_pk):
	player = request.user.company
	company_average = CompanyStorage.objects.exclude(company=request.user.company).filter(element=element_pk).aggregate(Avg('price'))['price__avg']
	company_average = int(round(company_average))
	planet_average = PlanetStorage.objects.all().filter(element=element_pk).aggregate(Avg('price'))['price__avg']
	planet_average = int(round(planet_average))
	element = get_object_or_404(Element, pk=element_pk)
	companyelements = CompanyStorage.objects.exclude(company=request.user.company).filter(element=element_pk).order_by('price')[:10:1]
	return render(request, "filterelement.html", {'companyelements': companyelements, 'planet_average': planet_average, 'company_average' : company_average, 'element' : element, 'player': player}) 

@login_required(login_url='/login/')
def planet_prices(request, element_pk):
	player = request.user.company
	planet_average = PlanetStorage.objects.all().filter(element=element_pk).aggregate(Avg('price'))['price__avg']
	planet_average = int(round(planet_average))
	company_average = CompanyStorage.objects.exclude(company=request.user.company).filter(element=element_pk).aggregate(Avg('price'))['price__avg']
	company_average = int(round(company_average))
	element = get_object_or_404(Element, pk=element_pk)
	planetelements = PlanetStorage.objects.all().filter(element=element_pk).order_by('-price')[:10:1]
	return render(request, "planetprices.html", {'planetelements': planetelements, 'company_average': company_average, 'planet_average' : planet_average, 'element' : element, 'player': player}) 