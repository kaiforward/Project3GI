# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from accounts.models import User
import random

class Element(models.Model):

	name = models.CharField(max_length=50)
	tag = models.CharField(max_length=5)
	weight = models.FloatField()
	color = models.CharField(max_length=20)
	rarity = models.IntegerField(default=1)

	def __unicode__(self):
		return self.name + ' - ' + str(self.rarity)	
