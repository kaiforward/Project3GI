# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

class Upgrade(models.Model):
	# Readable Info
	name = models.CharField(max_length=50)
	price = models.IntegerField()	
	production_increase = models.IntegerField()
	random_find_chance = models.IntegerField()
	random_find_increase = models.IntegerField()
	desc = models.TextField(max_length=500)
	image = models.ImageField(upload_to='images', blank=True, null=True)

	def __unicode__(self):
		return self.name

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
	real_price=models.IntegerField(default=0)
	# how much is mined, and the modifier for the mine size
	production = models.IntegerField()
	mine_size_mod = models.IntegerField()
	# Upgrade Level
	level = models.CharField(max_length=50, choices=LEVEL_CHOICE, default=LVL_1)
	image = models.ImageField(upload_to='images', blank=True, null=True)

	@property
	def paypal_form(self):
	    paypal_dict = {
	        "business": settings.PAYPAL_RECEIVER_EMAIL,
	        "amount": self.level,
	        "currency": "USD",
	        "item_name": self.mine_size,
	        "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
	        "notify_url": settings.PAYPAL_NOTIFY_URL,
	        "return_url": "%s/paypal-return" % settings.SITE_URL,
	        "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
	    }

	    return PayPalPaymentsForm(initial=paypal_dict)	

	def __unicode__(self):
		return self.mine_size


