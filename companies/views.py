# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, CompanyStorage, CompanyTrade, Ownership, MineOwnership, PlanetTrade
from ships.models import Spaceship 
from mining.models import Mine
from elements.models import Element
from planets.models import Planet, PlanetStorage, PlanetType
from .forms import CompanyForm, EditForm, PriceForm, TradeForm, PlanetTradeForm
from django.db.models import Avg
from django.utils import timezone
import random
from datetime import timedelta
# Create your views here.

@login_required(login_url='/login/')
def new_company(request):
    if request.method == "POST":            
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            # company creation
            company = form.save(commit=False)          
            company.user = request.user 
            company.locationx = random.randint(1, 10000)
            company.locationy = random.randint(1, 10000)
            company.locationz = random.randint(1, 10000)
            company.last_checked = timezone.now() - timedelta(days=1)
            company.save()
            elements = Element.objects.all() # get all element objects
            ship = get_object_or_404(Spaceship, ship='Cargo-Glork')
            mine = get_object_or_404(Mine, mine_size='Tiny')
            mine_element = random.choice(elements)
            first_ship = Ownership.objects.create_ship(ship, request.user.company)
            first_ship.amount = 1
            first_ship.save()
            first_mine = MineOwnership.objects.create_mine(mine, mine_element, request.user.company)
            first_mine.amount = 1
            first_mine.save()            
            for element in elements: # assign company ability to own each
                company_element = CompanyStorage.objects.give_company_elements(request.user.company, element) 
            
            # create new planets each time a new player joins
            planet_types = PlanetType.objects.all()
            elements = Element.objects.all()
            
            new_planet = Planet.objects.create_planet(planet_types)
            chosen_elements = random.sample(elements, 10)
            for element in chosen_elements:
                add_element = PlanetStorage.objects.change_planet_prices(new_planet, element, element.rarity)
                    
            return redirect(company_profile)
    else:
        form = CompanyForm()
    return render(request, 'profileform.html', {'form': form, 'user': request.user})

@login_required(login_url='/login/')
def company_profile(request):
    try:
        company = request.user.company

        mines_prod = MineOwnership.objects.mine_elements(company)
         
        trade_check = CompanyTrade.objects.check_trade_status(company)
        sale_check = PlanetTrade.objects.check_planet_trade_status(company)

        
        companyelements = CompanyStorage.objects.filter(company=company)
        trades = CompanyTrade.objects.filter(buyer=company).order_by('-date_to_finish')[:10]
        sales = PlanetTrade.objects.filter(seller=company).order_by('-date_to_finish')[:10]

        mines = MineOwnership.objects.filter(owner=company)
        ships = Ownership.objects.filter(owner=company)    
        return render(request, "profilepage.html", {
            'company': company,
            'companyelements' : companyelements, 
            'trades' : trades, 
            'mines_prod': mines_prod,
            'mines': mines,
            'ships': ships,
            'sales': sales,
            })
    except Company.DoesNotExist:
        return redirect(new_company)       
    
@login_required(login_url='/login/')
def all_companies(request):
    companies = Company.objects.exclude(user=request.user)
    return render(request, "companiespage.html", {'companies': companies, 'player': request.user.company})

@login_required(login_url='/login/')
def company_detail(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    company_elements = CompanyStorage.objects.filter(company=company)
    return render(request, "companydetail.html", {'company': company, 'player': request.user.company, 'companyelements': company_elements})

@login_required(login_url='/login/')
def edit_company(request):
    try:        
        company = request.user.company
    except Company.DoesNotExist:
        return redirect(new_company)  
    if request.method == "POST":
        form = EditForm(request.POST, request.FILES, instance=company) #instance fills out fields
        if form.is_valid():
            company = form.save(commit=False)          
            company.user = request.user # player name, is username (foreign_key)
            company.save()
            return redirect(company_profile)
    else:
        form = EditForm(instance=company)
    return render(request, 'editprofile.html', {'form': form})

@login_required(login_url='/login/')
def element_price(request, element_id): 
    companyelement = get_object_or_404(CompanyStorage, pk=element_id)
    if request.method == "POST":
        form = PriceForm(request.POST, request.FILES, instance=companyelement)
        if form.is_valid():
            companyelement = form.save(commit=False)
            companyelement.save()
            return redirect(company_profile) # redirect to player profile
    else:       
        form = PriceForm(instance=companyelement)
    average = CompanyStorage.objects.exclude(company=request.user.company).filter(element=companyelement.element).aggregate(Avg('price'))['price__avg']
    average = round(average, 2)
    return render(request, "elementprice.html", {'companyelement': companyelement, 'form': form, 'average' : average})

@login_required(login_url='/login/')
def company_trade(request, seller_pk, storage_pk):
    player = request.user.company    
    company_element = get_object_or_404(CompanyStorage, pk=storage_pk)
    player_element = get_object_or_404(CompanyStorage, element=company_element.element, company=player)
    company = get_object_or_404(Company, pk=seller_pk)
    if request.method == "POST":
        form = TradeForm(request.user.company, request.POST, request.FILES)
        if form.is_valid():
            trade = form.save(commit=False)
            owned = trade.ship
            # makes checks on trader info's
            if owned.in_use < owned.amount: # check player has a free ship
                if owned.ship.cargo_space >= trade.amount: # check if the ships storage space is large enough
                    if trade.amount > 0: # if valid number was inputted
                        if trade.amount * company_element.price <= player.money: # if player has enough money
                            if trade.amount <= company_element.amount: # and selling player has enough to sell
                                #make a sale
                                sale = CompanyTrade.objects.company_trade(company, company_element, trade.amount, request.user.company, owned)
                                messages.success(request, 'Thank you for your purchase! You can view your purchase on your company profile page.')
                                return redirect('elements') # redirect to player profile
                            else: # else return relevant error messages.
                                messages.error(request, 'This merchant does not have enough units')
                        else: 
                            messages.error(request, 'You do not have enough Glorks for that trade.')
                    else:
                        messages.error(request, 'You must select at least one.')
                else:
                    messages.error(request, "Your ship doesn't have enough space") 
            else:
                messages.error(request, 'You dont have any free Ships')
    else:       
        form = TradeForm(request.user.company)
    company_average = CompanyStorage.objects.exclude(company=request.user.company).filter(element=company_element.element).aggregate(Avg('price'))['price__avg'] 
    company_average = round(company_average, 2)
    planet_average = PlanetStorage.objects.all().filter(element=company_element.element).aggregate(Avg('price'))['price__avg'] 
    planet_average = round(planet_average, 2)
    return render(request, "companytrade.html", {'companyelement': company_element, 'form': form, 'company_average' : company_average, 'planet_average' : planet_average, 'player': player, 'playerelement': player_element})    

def trade_list(request):
    trades = CompanyTrade.objects.all().order_by('-date_created')[:20]
    return render(request, "tradelist.html", {'trades': trades})

@login_required(login_url='/login/')
def planet_trade(request, buyer_pk, storage_pk):
    player = request.user.company
    planet_element = get_object_or_404(PlanetStorage, pk=storage_pk)
    player_element = get_object_or_404(CompanyStorage, element=planet_element.element, company=player)
    planet = get_object_or_404(Planet, pk=buyer_pk)
    if request.method == "POST":
        form = PlanetTradeForm(request.user.company, request.POST, request.FILES)
        if form.is_valid():
            trade = form.save(commit=False)
            owned = trade.ship
            # makes checks on trader info's
            if owned.in_use < owned.amount: # check player has a free ship
                if owned.ship.cargo_space >= trade.amount: # check if the ships storage space is large enough
                    if trade.amount > 0: # if valid number was inputted                    
                        if trade.amount <= player_element.amount: # and selling player has enough to sell
                            #make a sale
                            sale = PlanetTrade.objects.planet_trade(request.user.company, planet_element, trade.amount, planet, owned)
                            messages.success(request, 'Thank you for Selling! You can view your sale info on your company profile page.')
                            return redirect('elements') # redirect to player profile
                        else: # else return relevant error messages.
                            messages.error(request, 'You do not have enough units')
                    else:
                        messages.error(request, 'You must select at least one.')
                else:
                    messages.error(request, "Your ship doesn't have enough space") 
            else:
                messages.error(request, 'You dont have any free Ships')
    else:       
        form = PlanetTradeForm(request.user.company)
    company_average = CompanyStorage.objects.exclude(company=request.user.company).filter(element=planet_element.element).aggregate(Avg('price'))['price__avg'] 
    Company_average = round(company_average, 2)
    planet_average = PlanetStorage.objects.all().filter(element=planet_element.element).aggregate(Avg('price'))['price__avg'] 
    planet_average = round(planet_average, 2)
    return render(request, "planettrade.html", {'planetelement': planet_element, 'form': form, 'company_average' : company_average, 'planet_average' : planet_average, 'player': player, 'playerelement': player_element})  