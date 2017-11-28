# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from elements.models import Element
from companies.models import Company, CompanyStorage
from django.shortcuts import redirect
from companies.models import CompanyTrade
from django.db.models import Avg, Max

# Create your views here.

@login_required(login_url='/login/')
def marketplace_view(request):

	cheapest = CompanyStorage.objects.exclude(company=request.user.company).order_by('-price')
	richest = Company.objects.exclude(name=request.user.company).order_by('money')[:1]
	trade = CompanyTrade.objects.all().order_by('-date_created')
	return render(request, "marketplace.html", {'cheapest': cheapest, 'richest': richest, 'trade': trade}) 

