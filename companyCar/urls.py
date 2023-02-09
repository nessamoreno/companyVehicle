from django.urls import path
from .views import *

urlpatterns = [
    path('listCar', VehicleList.as_view(), name='listVehicle'),
    path('listEmployee', EmployeeList.as_view(), name='listEmployee'),
    path('listClient', ClientList.as_view(), name='listClient'),
    path('listRent', RentList.as_view(), name='listRent')
]