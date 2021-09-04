from django import forms
from . models import Opros


class Opros_ModelForm(forms.ModelForm):
    class Meta:
        model = Opros
        exclude = ['creator', 'blocked']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'opisanie': forms.Textarea(attrs={"class": "form-control"}),
            'date_of_start': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'date_of_end': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
        labels = {
            "title": "*Название",
            "opisanie": "*Описание вопроса",
            "date_of_start": "дата старта (не требуется)",
            "date_of_end": "дата окончания (не требуется)",
        }
