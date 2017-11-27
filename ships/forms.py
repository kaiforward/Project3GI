# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from companies.models import Ownership

class ShipForm(forms.ModelForm):

    class Meta:
        model = Ownership
        fields = ('amount',)
