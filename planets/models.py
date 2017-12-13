# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from elements.models import Element
from language import word_creator, create_planet_affix
import random

# Create your models here.
class PlanetType(models.Model):

	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500)
	image = models.ImageField(upload_to='images', blank=True, null=True)

	def __unicode__(self):
		return self.name

class PlanetManager(models.Manager):

	def create_planet(self, planet_types):
		random_name = word_creator(random.randint(1, 2))
		random_affix = create_planet_affix()
		chosen_planet_type = random.choice(planet_types)
		planet = self.create(
			name = random_name+" "+random_affix,
			planet_type = chosen_planet_type,
			locationx = random.randint(1, 10000),
			locationy = random.randint(1, 10000),
			locationz = random.randint(1, 10000),
		)
		planet.save()
		return planet				

# Create your models here.
class Planet(models.Model):

	name = models.CharField(max_length=50)
	planet_type = models.ForeignKey(PlanetType, on_delete=models.CASCADE)
	locationx = models.IntegerField()	
	locationy = models.IntegerField()
	locationz = models.IntegerField()
	last_checked = models.DateTimeField(auto_now_add=True)

	objects = PlanetManager()

	def __unicode__(self):
		return self.name


class PlanetStorageManager(models.Manager):
	def change_planet_prices(self, planet_object, element_object, element_rarity):

		element_price = (random.randint(1, 10) + random.randint(10, 50)) * element_rarity

		if random.random() > 0.5:
			element_price += element_price / random.randint(17, 25)
		else:
			element_price -= element_price / random.randint(17, 25)
		round(element_price)

		planet_element = self.create(
			planet=planet_object,
			element=element_object,
			price= element_price,
		)			
		return planet_element	

class PlanetStorage(models.Model):

	planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
	element = models.ForeignKey(Element, on_delete=models.CASCADE)
	price = models.IntegerField(default=0)

	objects = PlanetStorageManager()

	def __unicode__(self):
		return str(unicode(self.planet) + ' - ' + unicode(self.element))