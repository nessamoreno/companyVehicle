from django import forms
from .models import *
class vehicleFormCreate(forms.ModelForm):
    vehicles = VehicleType.objects.all().values()
    veh_typ_id = forms.ModelChoiceField(
        queryset = vehicles,
        required=True,
        label="Seleccione el tipo de vehiculo",
        widget=forms.Select(attrs={"class" : "form-select", "style" : "font-size:14px"})
    )

    def __init__(self, *args, **kwargs):

        super(vehicleFormCreate, self).__init__(*args, **kwargs)

        self.fields['license_plate'].label = "Placa"

    class Meta:
        model = Vehicle
        fields = [
            'license_plate',
        ]

        widgets = {
            'license_plate' : forms.TextInput(attrs={"placeholder" : "Placa del vehiculo", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
        }

class EmployeeFormCreate(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(EmployeeFormCreate, self).__init__(*args, **kwargs)

        self.fields['identification'].label = "Identificación"
        self.fields['name'].label = "Nombre"
        self.fields['age'].label = "Edad"

    class Meta:
        model = Employee
        fields = [
            'identification',
            'name',
            'age'
        ]

        widgets = {
            'identification' : forms.NumberInput(attrs={"placeholder" : "Ingresa número de documento", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
            'name' : forms.TextInput(attrs={"placeholder" : "Ingresa nombre", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
            'age' : forms.NumberInput(attrs={"placeholder" : "Ingresa edad", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
        }

class ClientFormCreate(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(ClientFormCreate, self).__init__(*args, **kwargs)

        self.fields['identification'].label = "Identificación"
        self.fields['name'].label = "Nombre"
        self.fields['number'].label = "Número"
        self.fields['age'].label = "Edad"

    class Meta:
        model = Client
        fields = [
            'identification',
            'name',
            'number',
            'age'
        ]

        widgets = {
            'identification' : forms.NumberInput(attrs={"placeholder" : "Ingresa número de documento", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
            'name' : forms.TextInput(attrs={"placeholder" : "Ingresa nombre", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
            'number' : forms.NumberInput(attrs={"placeholder" : "Ingresa número de  celular", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
            'age' : forms.NumberInput(attrs={"placeholder" : "Ingresa edad", "class" : "form-control", "style" : "font-size: 14px; text-transform: uppercase;"}),
        }
    


class RentFormCreate(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(RentFormCreate, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = "Fecha de inicio"
        self.fields['final_date'].label = "Fecha de fin"

    class Meta:
        model = Rent
        fields = [
            'start_date',
            'final_date',
        ]

        widgets = {
            "start_date" : forms.DateInput(format='%Y-%m-%d', attrs={"class" : "form-control", "type" : "date", "style" : "font-size: 14px;"}),
            "final_date" : forms.DateInput(format="%Y-%m-%d", attrs={"class" : "form-control", "type" : "date", "style" : "font-size: 14px;"})
        }