# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
MK_1 = 'CL'
MK_2 = 'ZS'
MK_3 = 'F'

CHOICE = (
	(MK_1, 'Clarke Labs'),
	(MK_2, "Zorg's Shipyard"),
	(MK_3, 'Foundation'),
)

# Create your models here.
class Spaceship(models.Model):

	manufacturer = models.CharField(max_length=50, choices=CHOICE, default=MK_1)
	ship = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	speed = models.IntegerField()
	price = models.IntegerField()
	cargo_space = models.IntegerField()
	image = models.ImageField(upload_to='images', blank=True, null=True)

	def __unicode__(self):
		return self.ship + ' ' + self.manufacturer