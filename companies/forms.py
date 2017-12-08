from django import forms
from django.forms import ModelForm
from .models import Company, CompanyStorage, CompanyTrade, Ownership, PlanetTrade
 
class CompanyForm(forms.ModelForm):
 
    class Meta:
        model = Company
        fields = ('name', 'description', 'image', 'planets')

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

class PlanetTradeForm(forms.ModelForm):

    class Meta:
        model = PlanetTrade
        fields = ('amount', 'ship')
    # Custom Form allows player to choose which ship they want to transport their trade.

    # set init to take user variable that lets me target logged in user for ship field.
    def __init__(self, user, *args, **kwargs):
        super(PlanetTradeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['ship'].queryset = Ownership.objects.filter(owner=user)