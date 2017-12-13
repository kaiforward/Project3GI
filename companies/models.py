# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.forms import ModelForm
from datetime import datetime, timedelta
import random, math
from accounts.models import User
from elements.models import Element
from ships.models import Spaceship
from mining.models import Mine, Upgrade
from planets.models import Planet


# Planet types for selection
CONTINENTAL = 'CN'
TROPICAL = 'TR'
OCEANIC = 'OC'
DESERT = 'DS'
TUNDRA = 'TN'
PLANET_CHOICE = (
	(CONTINENTAL, 'Continental'),
	(TROPICAL, 'Tropical'),
	(OCEANIC, 'Oceanic'),
	(DESERT, 'Desert'),
	(TUNDRA, 'Tundra'),
)

# Create your models here.
class Company(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	locationx = models.IntegerField(default=0)
	locationy = models.IntegerField(default=0)
	locationz = models.IntegerField(default=5000)
	money = models.IntegerField(default=10000)
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(max_length=500)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	planets = models.CharField(max_length=2, choices=PLANET_CHOICE, default=CONTINENTAL)
	last_checked = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.name


class StorageManager(models.Manager):
	def give_company_elements(self, company_id, element_id):
		company_element = self.create(
			company=company_id,
			element=element_id,
			price= random.randint(50, 200),
			amount=random.randint(1, 50),
		)
		company_element.save()			
		return company_element	

class CompanyStorage(models.Model):

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	element = models.ForeignKey(Element, on_delete=models.CASCADE)
	amount = models.IntegerField()
	price = models.IntegerField()

	objects = StorageManager()

	def __unicode__(self):
		return str(unicode(self.company) + ' - ' + unicode(self.element))


class ShipManager(models.Manager):

	def create_ship (self, ship, buyer):
		new_ship = self.create(
			owner=buyer,
			ship=ship,
			amount=0,
			in_use=0,
		)
		return new_ship

	def add_ship (self, amount, ship, buyer):
		owned_ship = Ownership.objects.filter(owner=buyer, ship=ship)[0]
		owned_ship.amount += amount
		buyer.money -= ship.price * amount
		buyer.save()
		owned_ship.save()	

class Ownership(models.Model):

	owner = models.ForeignKey(Company, on_delete=models.CASCADE)
	ship = models.ForeignKey(Spaceship, on_delete=models.CASCADE)
	amount = models.IntegerField()
	in_use = models.IntegerField()

	objects = ShipManager()

	def __unicode__(self):
		return self.owner.name + ' - ' + self.ship.ship

class MineManager(models.Manager):

	def mine_elements(self, company):
		# This add Elements to a company over time.
		owned_mines = MineOwnership.objects.filter(owner=company)
		# get time difference between last time user is on profile screen
		time_multiplier = timezone.now() - company.last_checked 
		time_in_hours = time_multiplier.days * 24.0 + (time_multiplier.seconds / 3200.0)
		round(time_in_hours, 2) # rounds result in hours
		all_minerals = set()

		for owned in owned_mines: # iterate through all owned mines.
			mine = owned.mine # type of mine
			# target specific company storage of one element
			company_mineral = CompanyStorage.objects.filter(element=owned.element, company=company)[0]
			# add minerals based on time that has passed			
			mineral_added = (mine.production * mine.mine_size_mod * owned.amount) * time_in_hours
			mineral_added = round(mineral_added) # round to int as minerals only in ints
			if mineral_added > 0: # wait until enough time has passed for 1 to be created before resetting.	
				company_mineral.amount += mineral_added # add minerals to company
				company_mineral.save() # save result
				new_mineral = (mine.mine_size, owned.amount, company_mineral.element.name, mineral_added)			
				all_minerals.add(new_mineral)		 
				# prevent time resetting if no minerals were added (not enough time passed)
				company.last_checked = timezone.now()
				company.save()
		return all_minerals

	def create_mine (self, mine, element, buyer):
		new_mine = self.create(
			owner=buyer,
			mine=mine,
			element=element,
			amount=0,
		)
		return new_mine

	def add_mine (self, amount, element, mine, buyer):
		owned_mine = MineOwnership.objects.filter(owner=buyer, element=element, mine=mine)[0]
		owned_mine.amount += amount
		buyer.money -= mine.price * amount
		buyer.save()
		owned_mine.save()

class MineOwnership(models.Model):

	owner = models.ForeignKey(Company, on_delete=models.CASCADE)
	mine = models.ForeignKey(Mine, on_delete=models.CASCADE)
	element = models.ForeignKey(Element, on_delete=models.CASCADE)
	amount = models.IntegerField()
	upgrade = models.ForeignKey(Upgrade, on_delete=models.CASCADE, blank=True, null=True)

	objects = MineManager()

	def __unicode__(self):
		return self.owner.name + ' - ' + self.mine.mine_size

class TradeManager(models.Manager):
	def company_trade(self, seller, company_element, amount, buyer, owned_ship):

		owned_ship.in_use += 1
		owned_ship.save()
		buyer_storage = CompanyStorage.objects.filter(company=buyer, element=company_element.element)
		buyer_storage = buyer_storage[0]


		# locations/distance calculations for traders
		x = buyer.locationx
		x2 = seller.locationx
		y = buyer.locationy
		y2 = seller.locationy
		z = buyer.locationz
		z2 = seller.locationz
		distance = math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2) + (z-z2)*(z-z2))
		# work out fuel cost from distance
		fuel_cost = distance / 300 * amount
		round(fuel_cost)
		price = amount * company_element.price + fuel_cost
		# make a new trade
		trade = self.create(
			buyer=buyer,
			seller=seller,
			element=company_element.element,
			amount=amount,
			price=price,
			distance=distance,
			status='Pending',
			ship=owned_ship,
		)
		# find out when trade will finish
		ship_speed_multiplier = distance / owned_ship.ship.speed
		now = trade.date_created
		trade_finish_date = trade.date_created + timedelta(seconds=ship_speed_multiplier)
		trade.date_to_finish = trade_finish_date
		trade.save()

		company_element.amount -= amount
		company_element.save()
		seller.money += price		
		seller.save()

		buyer.money -= price		
		buyer.save()					
		return trade

	def check_trade_status(self, company):
		company_trades = CompanyTrade.objects.filter(buyer=company, status='Pending')

		for trade in company_trades:
			company_element = CompanyStorage.objects.filter(element=trade.element, company=company)[0]
			if timezone.now() >= trade.date_to_finish:
					trade.ship.in_use -= 1
					if trade.ship.in_use < 0:
						trade.ship.in_use = 0
					trade.ship.save()
					company_element.amount += trade.amount
					company_element.save()
					trade.status = 'Completed'
					trade.save()

class CompanyTrade(models.Model):

	buyer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='buyer_trade')
	seller = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='seller_trade')
	element = models.ForeignKey(Element, on_delete=models.CASCADE)
	amount = models.IntegerField()
	price = models.IntegerField()
	distance = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_to_finish = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=50)
	ship = models.ForeignKey(Ownership, on_delete=models.CASCADE)

	objects = TradeManager()

	def __unicode__(self):
		return self.buyer.name + ' - ' + self.seller.name

class PlanetTradeManager(models.Manager):
	def planet_trade(self, seller, planet_element, amount, buyer, owned_ship):

		owned_ship.in_use += 1
		owned_ship.save()
		seller_storage = CompanyStorage.objects.filter(company=seller, element=planet_element.element)
		seller_storage = seller_storage[0]

		# locations/distance calculations for traders
		x = buyer.locationx
		x2 = seller.locationx
		y = buyer.locationy
		y2 = seller.locationy
		z = buyer.locationz
		z2 = seller.locationz
		distance = math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2) + (z-z2)*(z-z2))
		# work out fuel cost from distance
		fuel_cost = distance / 300 * amount
		round(fuel_cost)
		price = amount * planet_element.price - fuel_cost
		# make a new trade
		trade = self.create(
			buyer=buyer,
			seller=seller,
			element=planet_element.element,
			amount=amount,
			price=price,
			distance=distance,
			status='Pending',
			ship=owned_ship,
		)
		# find out when trade will finish
		ship_speed_multiplier = distance / owned_ship.ship.speed
		now = trade.date_created
		trade_finish_date = trade.date_created + timedelta(seconds=ship_speed_multiplier)
		trade.date_to_finish = trade_finish_date
		trade.save()

		planet_element.price -= round(amount / random.randint(9, 18))
		planet_element.save()
		seller.money += price		
		seller.save()
		seller_storage.amount -= amount
		seller_storage.save()				
		return trade

	def check_planet_trade_status(self, company):
		planet_trades = PlanetTrade.objects.filter(seller=company, status='Pending')

		for trade in planet_trades:
			if timezone.now() >= trade.date_to_finish:
					trade.ship.in_use -= 1
					if trade.ship.in_use < 0:
						trade.ship.in_use = 0
					trade.ship.save()
					trade.status = 'Completed'
					trade.save()

class PlanetTrade(models.Model):

	buyer = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='planet_buyer_trade')
	seller = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='planet_seller_trade')
	element = models.ForeignKey(Element, on_delete=models.CASCADE)
	amount = models.IntegerField()
	price = models.IntegerField()
	distance = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_to_finish = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=50)
	ship = models.ForeignKey(Ownership, on_delete=models.CASCADE)

	objects = PlanetTradeManager()

	def __unicode__(self):
		return self.buyer.name + ' - ' + self.seller.name