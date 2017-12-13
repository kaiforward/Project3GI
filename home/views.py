# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ships.models import Spaceship
from mining.models import Mine
from planets.models import PlanetType
import random 

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
	ships = Spaceship.objects.all()
	ship = random.choice(ships)
	mines = Mine.objects.all()
	mine = random.choice(mines)
	return render(request, 'about.html', {'ship': ship, 'mine': mine,})