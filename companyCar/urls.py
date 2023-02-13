from django.urls import path
from .views import *
from . import views

app_name = "companyCar"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('listCar', VehicleList.as_view(), name='listVehicle'),
    path('createCar', VehicleCreate.as_view(), name='createVehicle'),
    path('listEmployee', EmployeeList.as_view(), name='listEmployee'),
    path('createEmployee', EmployeeCreate.as_view(), name='createEmployee'),
    path('listClient', ClientList.as_view(), name='listClient'),
    path('createClient',ClientCreate.as_view(), name='createClient'),
    path('listRent', RentList.as_view(), name='listRent'),
    path('createRent', RentCreate.as_view(), name='createRent')
]