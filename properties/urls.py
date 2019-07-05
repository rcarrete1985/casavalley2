from django.urls import path
from . import views

urlpatterns = [
    # URL to auctioned link on main navigation bar
    path('auctioned', views.Auctioned, name='auctioned'),
    # URL to delete a property using buttons
    path('delete/<propertyId>',  views.Delete, name='delete'),
    # URL to view or update property details
    path('<propertyId>', views.Details, name='details'),
    # URL to main home page which allows adding properties and has watchlist
    path('', views.Home, name='home'),
]
