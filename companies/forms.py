from django import forms
from django.forms import ModelForm
from .models import Company, CompanyStorage, CompanyTrade, Ownership, User
 
class CompanyForm(forms.ModelForm):
 
    class Meta:
        model = Company
        fields = ('name', 'description', 'image', 'planets')
	# def clean_name(self):
	# 	name = self.cleaned_data.get('name')
	# 	if name and Company.objects.filter(name=name):
	# 		message = 'Sorry this name has already been trademarked.'
	# 		raise ValidationError(message)
	# 	else:
	# 		return name # think this works? 

class EditForm(forms.ModelForm):
 
    class Meta:
        model = Company
        fields = ('name', 'description', 'image')

class PriceForm(forms.ModelForm):
 
    class Meta:
        model = CompanyStorage
        fields = ('price',)

class TradeForm(forms.ModelForm):

    class Meta:
        model = CompanyTrade
        fields = ('amount', 'ship')
    # Custom Form allows player to choose which ship they want to transport their trade.

    # set init to take user variable that lets me target logged in user for ship field.
    def __init__(self, user, *args, **kwargs):
        super(TradeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['ship'].queryset = Ownership.objects.filter(owner=user)