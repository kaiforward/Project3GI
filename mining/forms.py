# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from companies.models import MineOwnership, Company

class MineForm(forms.ModelForm):

    class Meta:
        model = MineOwnership
        fields = ('amount', 'element')
