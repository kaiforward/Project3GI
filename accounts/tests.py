# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import User
from django.shortcuts import render_to_response
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings
# Create your tests here.

class UserLogin(TestCase):

	def setUp(self):
		super(UserLogin, self).setUp()
		self.user = User.objects.create(username = 'testuser')
		self.user.set_password('opensesame')
		self.user.save()

	def test_login(self):
		login = self.client.login(username='testuser', password='opensesame')
		self.assertTrue(login)

	def test_registration_form(self):
	    form = UserRegistrationForm({
	        'email': 'test@test.com',
	        'password1': 'letmein1',
	        'password2': 'letmein1',
	        'stripe_id': settings.STRIPE_SECRET,
	        'credit_card_number': 4242424242424242,
	        'cvv': 123,
	        'expiry_month': 1,
	        'expiry_year': 2033
	    })
	    self.assertTrue(form.is_valid())
