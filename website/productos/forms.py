from django import forms
from .models import Suscriptor

class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = ['nombre', 'correo_electronico']
