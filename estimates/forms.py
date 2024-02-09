from django import forms
from .models import Estimate

class SingleEstimateMOdelForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = '__all__'
    