from django import forms
from .models import Piso

class PisoForm(forms.ModelForm):
    class Meta:
        model = Piso
        fields = ['numero_piso']