# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from elements.models import Element
from companies.models import Company, CompanyStorage, CompanyTrade
from planets.models import PlanetStorage
from .models import Story
from django.db.models import Avg, Max
import random

# Create your views here.
@login_required(login_url='/login/')
def marketplace_view(request):
    try:
		company = request.user.company
		stories = Story.objects.all()
		chosen_story = random.choice(stories)
		#best prices
		highest_element = PlanetStorage.objects.all().order_by('-price')[:5]
		# get cheapest elements excluding logged in player
		cheapest_element = CompanyStorage.objects.exclude(company=request.user.company).order_by('price')[:5]
		# get wealthiest companies including logged in player
		richest_company = Company.objects.all().order_by('-money')[:5] 
		# show most recent trade excluding logged in player
		recent_trade = CompanyTrade.objects.exclude(buyer=request.user.company).order_by('-date_created')[:1]
		return render(request, "marketplace.html", {'cheapest': cheapest_element, 'richest': richest_company, 'trade': recent_trade, 'story': chosen_story, 'highest': highest_element})     
    except Company.DoesNotExist:
        return redirect(new_company) 


def story_detail(request, story_pk):
	chosen_story = get_object_or_404(Story, pk=story_pk)
	return render(request, "storydetail.html", {'story': chosen_story}) 

