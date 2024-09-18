from django import forms
from .models import Personajes

class CrearPersonajeForm(forms.ModelForm):
    class Meta:
        model= Personajes
        fields= ['nombre','elemental','arma','vision','ultimate','decripcion','decripcion_elemental','decripcion_ultimate','img']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=50)

class EliminarForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())