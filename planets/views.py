# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PlanetType, Planet, PlanetStorage
from django.utils import timezone
from datetime import datetime, timedelta
from elements.models import Element
import random
# Create your views here.
@login_required(login_url='/login/')
def all_planets(request):
	player = request.user.company
	view_planets = Planet.objects.all()[:10]	
	return render(request, "planets.html", {'planets': view_planets, 'player': player}) 

@login_required(login_url='/login/')
def planet_detail(request, planet_pk):
	player = request.user.company
	planet = get_object_or_404(Planet, pk=planet_pk)
	planet_elements = PlanetStorage.objects.filter(planet=planet)	
	return render(request, "planetdetail.html", {'planet': planet, 'planetelements': planet_elements, 'player': player}) 

@login_required(login_url='/login/')
def create_planets_view(request):
	planet_types = PlanetType.objects.all()
	new_planet = Planet.objects.create_planet(planet_types)

	elements = Element.objects.all()
	chosen_elements = random.sample(elements, 10)
	
	for element in chosen_elements:
		add_element = PlanetStorage.objects.change_planet_prices(new_planet, element, element.rarity)
	
	planet_elements = PlanetStorage.objects.filter(planet=new_planet)
	
	return render(request, "newplanet.html", {'planet': new_planet, 'elements': planet_elements}) 

@login_required(login_url='/login/')
def update_planet_prices(request):

	all_planets = Planet.objects.all()
	
	for planet in all_planets:
		if planet.last_checked + timedelta(days=1) <= timezone.now():
			remove_old_prices = PlanetStorage.objects.filter(planet=planet).delete()
			elements = Element.objects.all()
			chosen_elements = random.sample(elements, 10)
			for element in chosen_elements:
				add_element = PlanetStorage.objects.change_planet_prices(planet, element, element.rarity)		
	
	view_planets = Planet.objects.all()[:10]

	return render(request, "planetsupdated.html", {'planets': view_planets}) 

