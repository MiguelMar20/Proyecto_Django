from django import forms
from Apps.Aplicacion1.models import Actividades

class Aplicacion1Form(forms.ModelForm):
    class Meta:
        model = Actividades
        
        fields = [
            'nombre_de_actividad',
            'sector_asignado',
            'objetivo',
            'monto_planificado',
            'periodo',
        ]
        labels = {
            'nombre_de_actividad': 'Nombre de la actividad',
            'sector_asignado': 'Sector encargado',
            'objetivo':'Objetivo de la actividad',
            'monto_planificado':'Monto disponible',
            'periodo':'Tiempo de ejecución',
        } 
        widgets = {
            'nombre_de_actividad': forms.TextInput(attrs={'class':'form-control'} ),
            'sector_asignado':forms.TextInput(attrs={'class':'form-control'}),
            'objetivo':forms.TextInput(attrs={'class':'form-control'} ),
            'monto_planificado':forms.TextInput(attrs={'class':'form-control'}),
            'periodo':forms.TextInput(attrs={'class':'form-control'}),
        } 