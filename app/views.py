from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . forms import Opros_ModelForm, New_vopros_text_ModelForm
from . models import Opros, Question_tekst

#API: 
from rest_framework import mixins
from rest_framework import generics

from app.serializer import OprosSerializer, Question_tekst_Serializer



def index(request):
    user_ip = get_client_ip(request)
    return render(request, "app/index.html", {
        "user_ip": user_ip,
    })


# страница с деталями конкретного опроса
def opros_detailed(request, opros_id):
    current_opros = Opros.objects.get(pk=opros_id)
    # все вопросы с текстом к опросу
    questions_tekst = current_opros.question_for_opros.all()
    #print(questions_tekst)
    
    return render(request, "app/opros_detailed.html",{
        "current_opros": current_opros,
        "questions_tekst": questions_tekst,
    })


# создание нового текстового вопроса
def new_vopros_text(request, opros_id):
    if request.method == "POST":
        form_new_vopros = New_vopros_text_ModelForm(request.POST)
        if form_new_vopros.is_valid():
            user = request.user
            question_text = form_new_vopros.cleaned_data['question_text']
            kakoy_opros = Opros.objects.get(pk=opros_id)
            new_vopros = Question_tekst(opros_id=kakoy_opros, question_text=question_text)
            new_vopros.save()
        return HttpResponseRedirect(reverse("opros_detailed", args=[opros_id]))

    else:
        blank_form_new_vopros = New_vopros_text_ModelForm()
        return render(request, "app/new_edit_vopros_text.html", {
            "blank_form_new_vopros": blank_form_new_vopros,
            "opros_id": opros_id,
            "message": "Здесь форма нового вопроса с текстом для опроса для админа: ",
            "new": True,
        })

# изменение существующего текстового вопроса
def edit_vopros_text(request, vopros_id):
    if request.method == "POST":
        form_edit_vopros = New_vopros_text_ModelForm(request.POST)
        if form_edit_vopros.is_valid():
            question_text = form_edit_vopros.cleaned_data['question_text']
            kakoy_vopros = Question_tekst.objects.get(pk=vopros_id)            
            kakoy_vopros.question_text = question_text
            kakoy_vopros.save()
            
            
            current_vopros = Question_tekst.objects.filter(pk=vopros_id).first()
            opros_id = current_vopros.opros_id.id            
            return HttpResponseRedirect(reverse("opros_detailed", args=[opros_id]))
            

    else:
        blank_form_edit_vopros = New_vopros_text_ModelForm()
        current_vopros = Question_tekst.objects.filter(pk=vopros_id).first()
        #opros_id = current_vopros.opros_id.id
        #print(opros_id)
        return render(request, "app/new_edit_vopros_text.html", {
            "current_vopros": current_vopros,
            "blank_form_edit_vopros": blank_form_edit_vopros,
            "vopros_id": vopros_id,
            "message": "Здесь форма изменение конкретного вопроса: ",
            "edit": True,
        })

# удаление вопроса из опроса
def delete_vopros_text(request, vopros_id):
    current_vopros = Question_tekst.objects.filter(pk=vopros_id).first()
    opros_id = current_vopros.opros_id.id
    
    vopros_to_delete = Question_tekst.objects.get(pk=vopros_id)
    vopros_to_delete.delete()
    return HttpResponseRedirect(reverse("opros_detailed", args=[opros_id]))

        

def list_admin(request):
    all_opros = Opros.objects.all()
    return render(request, "app/list_admin.html", {
        "all_opros": all_opros,
    })


def new_opros(request):
    if request.method == "POST":
        form_new_opros = Opros_ModelForm(request.POST)
        if form_new_opros.is_valid():
            user = request.user
            title = form_new_opros.cleaned_data['title']            
            date_of_start = form_new_opros.cleaned_data['date_of_start']
            date_of_end = form_new_opros.cleaned_data['date_of_end']
            new_opros = Opros(title=title, creator=user, date_of_start=date_of_start, date_of_end=date_of_end)
            new_opros.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        blank_form_new_opros = Opros_ModelForm()
        return render(request, "app/new_edit_opros.html", {
            "blank_form_new_opros": blank_form_new_opros,
            "message": "Форма для СОЗДАНИЯ нового опроса: ",
            "create_opros" : True,
        })


def edit_opros(request, opros_id):
    if request.method == "POST":
        form_new_opros = Opros_ModelForm(request.POST)
        if form_new_opros.is_valid():
            user = request.user
            title = form_new_opros.cleaned_data['title']
            date_of_start = form_new_opros.cleaned_data['date_of_start']
            date_of_end = form_new_opros.cleaned_data['date_of_end']
            new_opros = Opros(title=title, creator=user,
                              date_of_start=date_of_start, date_of_end=date_of_end)
            new_opros.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        blank_form_edit_opros = Opros_ModelForm()
        return render(request, "app/new_edit_opros.html", {
            "blank_form_edit_opros": blank_form_edit_opros,
            "message": "Форма для ИЗМЕНЕНИЯ старого опроса: ",
            "edit_opros": True,
            "opros_id": opros_id,
        })


# IP каждго юзера. This is "id" of any unauthorized user.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



# API
# Лист опросов - все опросы
class List_Opros_api(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Opros.objects.all()
    serializer_class = OprosSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
# Детальные опросы (по штучно) - GET - PUT - CREATE - DELETE
class Detailed_Opros_api(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView,):
    queryset = Opros.objects.all()
    serializer_class = OprosSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# все опросы с ответом текстом (лист опросов)
class Question_tekst_api(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Question_tekst.objects.all()
    serializer_class = Question_tekst_Serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Question_tekst_detailed(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView,):
    queryset = Question_tekst.objects.all()
    serializer_class = Question_tekst_Serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




