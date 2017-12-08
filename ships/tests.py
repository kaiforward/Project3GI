# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from ships.views import ships_all
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .models import Spaceship

# Create your tests here. 
 
 
class ShipsPageTest(TestCase):

	fixtures = ['ships']

	def test_ship_page_resolves(self):
	    ships_page = resolve('/marketplace/ships/all/')
	    self.assertEqual(ships_page.func, ships_all)
 
	# def test_check_content_is_correct(self):
	#     ships_page = self.client.get('/marketplace/ships/all/')
	#     self.assertTemplateUsed(ships_page, "ships.html")
	#     ships_page_template_output = render_to_response("ships.html", {'ships': Spaceship.objects.all()}).content                                                         
	#     self.assertEqual(ships_page.content, ships_page_template_output)