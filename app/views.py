from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

#from . forms import Opros_ModelForm
#from . models import Opros
# Create your views here.


def index(request):
    # user_ip = get_client_ip(request)
    return render(request, "app/index.html", {
        # "user_ip": user_ip,
    })


# def list_admin(request):
#     all_opros = Opros.objects.all()
#     return render(request, "app/list_admin.html", {
#         "all_opros": all_opros,
#     })


# def new_opros(request):
#     if request.method == "POST":
#         form_new_opros = Opros_ModelForm(request.POST)
#         if form_new_opros.is_valid():
#             user = request.user
#             title = form_new_opros.cleaned_data['title']
#             new_opros = Opros(title=title, creator=user)
#             new_opros.save()
#         return HttpResponseRedirect(reverse("index"))

#     else:
#         blank_form_new_opros = Opros_ModelForm()
#         return render(request, "app/new_opros.html", {
#             "blank_form_new_opros": blank_form_new_opros,
#         })


# # IP каждго юзера. This is "id" of any unauthorized user.
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
