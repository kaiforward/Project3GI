from django import forms

from .models import Company, CompanyStorage, CompanyTrade
 
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
        fields = ('amount',)

