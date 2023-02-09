from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpRequest
# from django.views import View
# from django.views import *
# from django.http.response import JsonResponse
# from django.http.request import JsonRequest
from django.views import generic
from .models import *
from django.db.models import F
# Create your views here.

class VehicleList(generic.ListView):
    model = Vehicle
    template_name = 'vehicle.html'

    def get_context_data(self, **kwargs):
        context = super(VehicleList, self).get_context_data(**kwargs)
        vehicles = Vehicle.objects.all().annotate(vehicle_type = F('veh_typ_id__type')).annotate(vehicle_price= F('veh_typ_id__price')).values()
        context['vehicle'] = vehicles

        return context
    
class EmployeeList(generic.ListView):
    model = Employee
    template_name = 'employee.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        employees = Employee.objects.all().values()
        context['employee'] = employees

        return context

class ClientList(generic.ListView):
    model = Client
    template_name = 'client.html'

    def get_context_data(self, **kwargs):
        context = super(ClientList,self).get_context_data(**kwargs)
        clients = Client.objects.all().values()
        context['client'] = clients

        return context

class RentList(generic.ListView):
    model = Rent
    template_name = 'rent.html'

    def get_context_data(self, **kwargs):
        context = super(RentList,self).get_context_data(**kwargs)
        rents = Rent.objects.all().annotate(licen_plate = F('veh_id_id__license_plate')).annotate(name_client = F('cli_id_id__name')).annotate(name_employee = F('emp_id_id__name')).annotate(type = F ('veh_id_id__veh_typ_id_id__type')).annotate(price = F ('veh_id_id__veh_typ_id_id__price')).values()
        context['rent'] = rents

        return context