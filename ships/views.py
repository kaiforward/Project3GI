# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Spaceship
from .forms import ShipForm
from companies.models import Ownership

# Create your views here.
@login_required(login_url='/login/')
def ships_all(request):
	ships = Spaceship.objects.all()
	return render(request, "ships.html", {'ships': ships}) 

@login_required(login_url='/login/')
def ship_detail(request, ship_pk):
	ship = get_object_or_404(Spaceship, pk=ship_pk)
	if request.method == "POST":            
		form = ShipForm(request.POST, request.FILES)
		if form.is_valid():
			player = request.user.company
			owned_ship = form.save(commit=False)
			if owned_ship.amount > 0: # amount must be above zero
				if owned_ship.amount * ship.price < player.money:
				# refresh user mining so checked date is correct for new mines. 
					try: # find player mines of same type, if already exist, add another to amount of mines.
						player_ship = get_object_or_404(Ownership, owner=request.user.company, ship=ship)         
						sale = Ownership.objects.add_ship(owned_ship.amount, ship, request.user.company)   
						return redirect(ships_all)
					except: # if player mines not already exists, create empty one, then add amount.
						new_ship = Ownership.objects.create_ship(ship, request.user.company)
						sale = Ownership.objects.add_ship(owned_ship.amount, ship, request.user.company)
						return redirect(ships_all)		        	
				else:    
					messages.error(request, 'You cannot afford this Trade.')
			else:
				messages.error(request, 'You must choose at least one')
	else:		   
		form = ShipForm()
	return render(request, "shipdetail.html", {'ship': ship, 'form': form})
