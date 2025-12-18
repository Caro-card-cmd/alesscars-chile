from django import forms
from .models import agenda

class agendaForm(forms.ModelForm):
    class Meta:
        model = agenda
        fields = ['servicio', 'marca', 'modelo', 'descripcion', 'fecha', 'imagen']

