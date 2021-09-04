from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_opros/", views.new_opros, name="new_opros"),
    path("list_admin/", views.list_admin, name="list_admin"),
    path("opros_detailed/<int:opros_id>", views.opros_detailed, name="opros_detailed"),
]

