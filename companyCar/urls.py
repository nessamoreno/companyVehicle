from django.urls import path
from .views import *

urlpatterns = [
    path('listCar', Vehicle.as_view(), name='listVehicle'),
    path('listEmployee', Employee.as_view(), name='listEmployee'),
    # path('listClient', Client.as_view(), name='listClient'),
    # path('listRent', Rent.as_view(), name='listRent')
]