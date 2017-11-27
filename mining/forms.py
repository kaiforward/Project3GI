# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from companies.models import MineOwnership, Company

class MineForm(forms.ModelForm):

    class Meta:
        model = MineOwnership
        fields = ('amount', 'element')

	def enough_money(self):
		company = Company.objects.filter(name=request.user.company)
		amount = self.cleaned_data.get('amount')
		if amount > company.money:
			message = 'Sorry you do not have enough money.'
			raise ValidationError(message)
		else:
			return amount
