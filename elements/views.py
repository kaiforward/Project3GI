# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Element
from companies.models import CompanyStorage
from django.shortcuts import redirect
from companies.views import company_trade
from django.db.models import Avg

@login_required(login_url='/login/')
def element_view(request):
	elements = Element.objects.all()
	return render(request, "elements.html", {'elements': elements}) 

@login_required(login_url='/login/')
def filter_element(request, element_pk):
	player = request.user.company
	average = CompanyStorage.objects.exclude(company=request.user.company).filter(element=element_pk).aggregate(Avg('price'))['price__avg']
	average = round(average, 2)
	element = get_object_or_404(Element, pk=element_pk)
	companyelements = CompanyStorage.objects.exclude(company=request.user.company).filter(element=element_pk).order_by('price')[:10:1]
	return render(request, "filterelement.html", {'companyelements': companyelements, 'average' : average, 'element' : element, 'player': player}) 