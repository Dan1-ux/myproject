from django import forms
from .models import Prospect

class ProspectForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = ['name', 'phone', 'status']