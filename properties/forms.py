from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    address = forms.CharField(label='Street Address Only (No City or State)')
    account = forms.CharField(label='Account Number')
    legalDescription = forms.CharField(label='Legal Description')
    livingSF = forms.IntegerField(label='Living SF')
    landSF = forms.IntegerField(label='Land SF')
    yearBuilt = forms.IntegerField(label='Year Built')
    ownerName = forms.CharField(label='Owner Name')
    homeStead = forms.CharField(label='Home Stead (Y/N)')
    subjectToNotIncludedInSale = forms.IntegerField(label='Subject To (Not Included in Sale)')
    taxesCoveredInSuit = forms.IntegerField(label='Taxes Covered in Suit')
    totalTaxesOwed = forms.IntegerField(label='Total Taxes Owed')
    valuesAdjudged = forms.IntegerField(label='Total Adjudged Values')
    valuesCAD = forms.IntegerField(label='Total CAD Values')
    valuesLandCAD = forms.IntegerField(label='CAD Values Land')
    valuesBldgCAD = forms.IntegerField(label='CAD Values Building')
    zestimate = forms.IntegerField(label='Zestimate')
    startingBid = forms.IntegerField(label='Starting Bid')
    finalBid = forms.IntegerField(label='Winning Bid', required=False)
    notes = forms.CharField(label='Notes', widget=forms.Textarea, required=False)

    class Meta:
        model = Property
        fields = ('address', 'account', 'legalDescription', 'livingSF',
                  'landSF', 'yearBuilt', 'ownerName', 'homeStead',
                  'subjectToNotIncludedInSale', 'taxesCoveredInSuit',
                  'totalTaxesOwed', 'valuesAdjudged', 'valuesLandCAD',
                  'valuesBldgCAD', 'valuesCAD', 'zestimate', 'startingBid',
                  'finalBid', 'notes')

        def __init__(self, *args, **kwargs):
            super(PropertyForm, self).__init__(*args, **kwargs)
            self.fields['myfield'].widget.attrs.update({'class': 'myfieldclass'})
