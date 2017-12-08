# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.views import home_view
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
# Create your tests here. 

# checks that the url / for the homepage, mathes wthe result for the home_view
class HomePageTest(TestCase):
	
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, home_view)

	def test_home_page_status_code_is_ok(self):
		home_page = self.client.get('/')
		self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)

