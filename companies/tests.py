# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.conf import settings
from accounts.models import User
from .models import Company, CompanyTrade
from .forms import CompanyForm, PriceForm

# Create your tests here.
class CompanyProfile(TestCase):

	def profile_form_is_correct(self):
		form = CompanyForm({
			'name': 'anything',
			'description': 'anythingelse',
			'image': '',
			'planets': 'Tundra'
			})
		self.assertTrue(form.is_valid()) 

	def price_form_is_correct(self):
		form = PriceForm({
			'price': 1,
			})
		self.assertTrue(form.is_valid())                      
                                 


