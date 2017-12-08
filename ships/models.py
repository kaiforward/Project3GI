# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

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
	price = models.IntegerField(default=0)	
	cargo_space = models.IntegerField()
	image = models.ImageField(upload_to='images', blank=True, null=True)
	real_price = models.IntegerField(default=0)

	@property
	def paypal_form(self):
	    paypal_dict = {
	        "business": settings.PAYPAL_RECEIVER_EMAIL,
	        "amount": self.real_price,
	        "currency": "USD",
	        "item_name": self.ship,
	        "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
	        "notify_url": settings.PAYPAL_NOTIFY_URL,
	        "return_url": "%s/paypal-return" % settings.SITE_URL,
	        "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
	    }

	    return PayPalPaymentsForm(initial=paypal_dict)		

	def __unicode__(self):
		return self.ship + ' ' + self.manufacturer
