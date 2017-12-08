# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
 
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)
# Create your tests here.
