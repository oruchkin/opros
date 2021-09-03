from django import forms
from . models import Opros


class Opros_ModelForm(forms.ModelForm):
    class Meta:
        model = Opros
        exclude = ['creator']
        widgets = {
            'title': forms.Textarea(attrs={"class": "form-control"}),
        }
