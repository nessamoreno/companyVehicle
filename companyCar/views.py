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
        context['vehicles'] = vehicles

        return context
    
class EmployeeList(generic.ListView):
    model = Employee
    template_name = 'employee.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        employee = Employee.objects.all().values()
        context['employee'] = employee

        return context

class Client():
    def list_client(request):
        return render(request,'/clients/client.html')

class Rent():
    def list_rent(request):
        return render(request,'/clients/rent.html')