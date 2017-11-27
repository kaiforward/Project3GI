# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Element
from companies.models import Company, CompanyStorage
from django.shortcuts import redirect
from companies.views import company_trade
from django.db.models import Avg, Max

@login_required(login_url='/login/')
def marketplace_view(request):

	cheapest = CompanyStorage.objects.exclude(company=request.user.company).aggregate(Max('-price'))[:1]
	cheapest = cheapest['price__avg']
	richest = Company.objects.exclude(company=request.user.company).aggregate(Max('money'))[:1]
	richest = richest['price__max']
	trade = CompanyTrade.objects.all().order_by('-date_created')[:1]

	return render(request, "makretplace.html", {'cheapest': cheapest, 'richest': richest, 'trade': trade}) 
# Create your views here.
