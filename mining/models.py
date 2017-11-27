# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
LVL_1 = 'ME'
LVL_2 = 'MD'
LVL_3 = 'MI'
LEVEL_CHOICE = (
	(LVL_1, 'Matter Extractor'),
	(LVL_2, 'Matter Devourer'),
	(LVL_3, 'Matter Inhaler'),
)
class Mine(models.Model):
	# Readable Info
	mine_size = models.CharField(max_length=50)	
	price = models.IntegerField()
	# how much is mined, and the modifier for the mine size
	production = models.IntegerField()
	mine_size_mod = models.IntegerField()
	# Upgrade Level
	level = models.CharField(max_length=50, choices=LEVEL_CHOICE, default=LVL_1)
	image = models.ImageField(upload_to='images', blank=True, null=True)

	def __unicode__(self):
		return self.mine_size

