from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.views import generic
from .models import *
from django.db.models import F
# Create your views here.


#CREATE VIEW MAIN
class Index(generic.TemplateView):
    template_name = 'index.html'


# CREATE CLASS VEHICLE LIST
class VehicleList(generic.ListView):
    model = Vehicle
    template_name = 'vehicle.html'

    def get_context_data(self, **kwargs):
        context = super(VehicleList, self).get_context_data(**kwargs)
        vehicles = Vehicle.objects.all().annotate(vehicle_type = F('veh_typ_id__type')).annotate(vehicle_price= F('veh_typ_id__price')).order_by('id').values()
        context['vehicle'] = vehicles

        return context

# CREATE CLASS VEHICLE CREATE
class VehicleCreate(generic.FormView):
    template_name = 'vehicle_create_form.html'
    model = Vehicle
    form_class = vehicleFormCreate

    def get_context_data(self, **kwargs):
        context = super(VehicleCreate, self).get_context_data(**kwargs)
        vehicles_type = VehicleType.objects.all().values()
        context['vehicles_type'] = vehicles_type

        return context

    def form_valid(self, form):
        d_license_plate = form.cleaned_data['license_plate']
        d_veh_typ_id = form.cleaned_data['veh_typ_id']
        print(d_veh_typ_id['id'])
        tipo_vehiculo = VehicleType.objects.get(id=d_veh_typ_id['id'])
        dataVehicle = Vehicle(
            license_plate = d_license_plate,
            veh_typ_id = tipo_vehiculo
        )

        dataVehicle.save()

        return HttpResponseRedirect(reverse("companyCar:listVehicle"))

#CREATE CLASS EMPLOYEE LIST
class EmployeeList(generic.ListView):
    model = Employee
    template_name = 'employee.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        employees = Employee.objects.all().values()
        context['employee'] = employees

        return context

#CREATE CLASS EMPLOYEE CREATE
class EmployeeCreate(generic.FormView):
    template_name = 'employee_create_form.html'
    model = Employee
    form_class = EmployeeFormCreate

    def form_valid(self, form):
        identification = form.cleaned_data['identification']
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        dataEmployee = Employee(
            identification = identification,
            name = name,
            age = age
        )

        dataEmployee.save()

        return HttpResponseRedirect(reverse("companyCar:listEmployee"))

#CREATE CLASS CLIENT LIST
class ClientList(generic.ListView):
    model = Client
    template_name = 'client.html'

    def get_context_data(self, **kwargs):
        context = super(ClientList,self).get_context_data(**kwargs)
        clients = Client.objects.all().values()
        context['client'] = clients

        return context

#CREATE CLASS CLIENT CREATE
class ClientCreate(generic.CreateView):
    template_name = 'client_create_form.html'
    model = Client
    form_class = ClientFormCreate

    def form_valid(self, form):
        identification = form.cleaned_data['identification']
        name = form.cleaned_data['name']
        number = form.cleaned_data['number']
        age = form.cleaned_data['age']
        dataClient = Client(
            identification = identification,
            name = name,
            number = number,
            age = age
        )

        dataClient.save()

        return HttpResponseRedirect(reverse("companyCar:listClient"))

#CREATE CLASS RENT LIST
class RentList(generic.ListView):
    model = Rent
    template_name = 'rent.html'

    def get_context_data(self, **kwargs):
        context = super(RentList,self).get_context_data(**kwargs)
        rents = Rent.objects.all().annotate(licen_plate = F('veh_id_id__license_plate')).annotate(name_client = F('cli_id_id__name')).annotate(name_employee = F('emp_id_id__name')).annotate(type = F ('veh_id_id__veh_typ_id_id__type')).annotate(price = F ('veh_id_id__veh_typ_id_id__price')).values()
        context['rent'] = rents

        return context

#CREATE CLASS RENT CREATE
class RentCreate(generic.CreateView):
    template_name = 'rent_create_form.html'
    model = Rent
    form_class = RentFormCreate

    def get_context_data(self, **kwargs):
        context = super(RentCreate, self).get_context_data(**kwargs)
        vehicles = Vehicle.objects.all().values()
        employees = Employee.objects.all().values()
        clients = Client.objects.all().values()
        context['vehicles'] = vehicles
        context['employees'] = employees
        context['clients'] = clients

        return context

    def form_valid(self, form):
        d_start_date = form.cleaned_data['start_date']
        d_final_date = form.cleaned_data['final_date']
        id_client = int(self.request.POST.get('cli_id'))
        id_employee = int(self.request.POST.get('emp_id'))
        id_vehicle = int(self.request.POST.get('veh_id'))

        client = Client.objects.get(id=id_client)
        employee = Employee.objects.get(id=id_employee)
        vehicle = Vehicle.objects.get(id=id_vehicle)

        days = d_final_date - d_start_date 
        days = days.days
        base = 50

        if id_vehicle == 1:
            increment = days * 1.5
        elif id_vehicle == 2:
            increment = 2
        elif id_vehicle == 3:
            pass
        else:
            increment = 40
        

        d_amount_payable = base + increment

        dataClient = Rent(
            start_date = d_start_date,
            final_date = d_final_date,
            cli_id = client,
            emp_id = employee,
            veh_id = vehicle,
            amount_payable =d_amount_payable,
        )

        dataClient.save()

        return HttpResponseRedirect(reverse("companyCar:listRent"))