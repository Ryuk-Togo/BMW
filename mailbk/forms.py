from django import forms
from django.db import models
from .models import TmpFile

class TmpFileModelForm(forms.ModelForm):
    class Meta:
        model = TmpFile
        fields = ('fileName','attach')
        fields = '__all__'
        # widgets = {
        #     'todo_id': forms.HiddenInput(),
        # }


TmpFileModelFormSet = forms.modelformset_factory(
    TmpFile, form=TmpFileModelForm,
)
