from django import forms
from . models import Opros, Question_tekst

# форма создания нового опроса
class Opros_ModelForm(forms.ModelForm):
    class Meta:
        model = Opros
        exclude = ['creator', 'blocked']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'opisanie': forms.Textarea(attrs={"class": "form-control"}),
            'date_of_start': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'date_of_end': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
        labels = {
            "title": "*Название",
            "opisanie": "*Описание вопроса",
            "date_of_start": "дата старта (не требуется)",
            "date_of_end": "дата окончания (не требуется)",
        }

# форма создания нового вороса с текстовым ответом
class New_vopros_text_ModelForm(forms.ModelForm):
    class Meta:
        model = Question_tekst
        exclude = ['opros_id', 'question_answer']
        widgets = {            
            'question_text': forms.Textarea(attrs={"class": "form-control"}),
        }
        labels = {
            "question_text": "*Вопрос:",            
        }
