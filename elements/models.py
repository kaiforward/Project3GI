# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from accounts.models import User
import random

# element types maybe not use this
GAS = 'GAS'
LIQUID = 'LIQ'
SOLID = 'SOL'

STATE_CHOICE = (
	(GAS, 'Gas'),
	(LIQUID, 'Liquid'),
	(SOLID, 'Solid'),
)

class Element(models.Model):

	name = models.CharField(max_length=50)
	tag = models.CharField(max_length=5)
	weight = models.FloatField()
	color = models.CharField(max_length=20)
	rarity = models.IntegerField(default=1)
	state = models.CharField(max_length=3, choices=STATE_CHOICE, default=GAS)

	def __unicode__(self):
		return self.name +' - ' + self.state	
