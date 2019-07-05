from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import Property
from django.forms.models import model_to_dict
from django.forms.widgets import HiddenInput
from sklearn.externals import joblib


# Import liner regression machine learning model, created in machinelearning.py.
clf = joblib.load('cvestimate.pkl')


# Main home view after logging in and being redirected to url=home
def Home(request):
    # Workflow B [adding new property from url=home]
    if request.method == 'POST':
        if 'add' in request.POST:
            form = PropertyForm(request.POST)
            if form.is_valid():
                # Save new property to database
                form.save()
                # Calculate and save cvestimate using form address as identifier
                X = [[form.cleaned_data['valuesCAD'], form.cleaned_data['zestimate']]]
                y = (clf.predict(X))
                address = form['address']
                address = (address.value())
                Property.objects.filter(address=address).update(cvEstimate=int(y))
    # Workflow A [blank form on initial landing on url=home]
    form = PropertyForm()
    form.fields['finalBid'].widget = HiddenInput()
    # Watchlist only shows properties where finalBid is empty, others are moved to url=auction
    properties = Property.objects.filter(finalBid__isnull=True)
    return render(request, 'home.html', {'form': form, 'properties': properties})


# Property details extend on html when property is chosen from watchlist on homepage
def Details(request, propertyId):
    # Workflow B [adding new property from url=details]
    if request.method == 'POST':
        if 'add' in request.POST:
            form = PropertyForm(request.POST)
            if form.is_valid():
                # Save new property to database
                form.save()
                # Calculate and save cvestimate using form address as identifier
                X = [[form.cleaned_data['valuesCAD'], form.cleaned_data['zestimate']]]
                y = (clf.predict(X))
                address = form['address']
                address = (address.value())
                Property.objects.filter(address=address).update(cvEstimate=int(y))
    # Workflow C [updating previous property from url=details]
    if request.method == 'POST':
        if 'update' in request.POST:
            # Get pk of property to update from POST and update on database
            propertyToUpdate = Property.objects.get(pk=propertyId)
            detailform = PropertyForm(request.POST, instance=propertyToUpdate)
            if detailform.is_valid():
                detailform.save()
                # Calculate and save cvestimate using form address as identifier
                X = [[int(detailform['valuesCAD'].value()), int(detailform['zestimate'].value())]]
                y = (clf.predict(X))
                address = detailform['address']
                address = (address.value())
                Property.objects.filter(address=address).update(cvEstimate=int(y))

    # Workflow A [property details landing page]
    # Show empty form on top - add button moves to workflow B
    form = PropertyForm()
    form.fields['finalBid'].widget = HiddenInput()
    # Watchlist only shows properties where finalBid is empty, others are moved to url=auction
    properties = Property.objects.filter(finalBid__isnull=True)
    # Show prepopulated from on bottom - update button moves to workflow C
    propertyDetail = Property.objects.get(pk=propertyId)
    detailform = PropertyForm(initial=model_to_dict(propertyDetail))
    return render(request, 'propertyDetails.html', {'form': form, 'detailform': detailform,
                                                    'properties': properties})


# Second top nav tab, watchlist of previous properties that have a final winning bid; used to train ML models
def Auctioned(request):
    properties = Property.objects.filter(finalBid__isnull=False)
    return render(request, 'Auctioned.html', {'properties': properties})


# Delete properties from either top nav tab
def Delete(request, propertyId):
    deleteProperty = Property.objects.get(id=propertyId)
    deleteProperty.delete()
    # Redirect redirect=home
    if 'home' in request.POST:
        return redirect('home')
    # Redirect url=auctioned
    else:
        return redirect('auctioned')
