from django import forms
from django.db import models
from .models import (
    TTodo,
    TDo,
)

# 本日のTODO
class NowTodoForm(forms.ModelForm):
    class Meta:
        model = TTodo
        fields = ('work_time','todo','complete',)
        widgets = {
            'work_time': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'work_time': forms.CharField(),
            'complete': forms.CheckboxInput,
        }

# 本日のTODO表示用
NowTodoModelFormSet = forms.formset_factory(
    form=NowTodoForm,
    extra=10,
)

# NowTodoModelFormSet = forms.modelformset_factory(
#     TTodo, 
#     form=NowTodoForm,
# )

# ---------------------------------------------------------
# DO入力
class InpuDoForm(forms.ModelForm):

    id = forms.IntegerField(label='主キー',
        required=False,
        widget=forms.HiddenInput(),
    )    
    
    class Meta:
        model = TDo
        fields = ('do','delivery_date')

# TODO入力
class InpuTodoForm(forms.ModelForm):

    id = forms.IntegerField(label='主キー',
        required=False,
        widget=forms.HiddenInput(),
    )    
    
    class Meta:
        model = TTodo
        fields = ('todo','row')
        widgets = {
            'row': forms.HiddenInput(),
        }

# TODO作成用
InputTodoModelFormSet = forms.formset_factory(
    form=InpuTodoForm,
)
# InputTodoModelFormSet = forms.modelformset_factory(
#     TTodo, 
#     form=InpuTodoForm,
# )
