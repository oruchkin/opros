from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),    
    path("list_admin/", views.list_admin, name="list_admin"),
    
    # создание-изменение-удаление и подробности ОПРОСА
    path("new_opros/", views.new_opros, name="new_opros"),
    path("edit_opros/<int:opros_id>", views.edit_opros, name="edit_opros"),
    path("opros_detailed/<int:opros_id>", views.opros_detailed, name="opros_detailed"),
    
    
    # ВОПРОС с текстом: создать-изменить-удалить
    path("new_vopros_text/<int:opros_id>", views.new_vopros_text, name="new_vopros_text"),
    path("edit_vopros_text/<int:vopros_id>", views.edit_vopros_text, name="edit_vopros_text"),
    path("delete_vopros_text/<int:vopros_id>", views.delete_vopros_text, name="delete_vopros_text"),
    
    # API
    path("list_opros/", views.List_Opros.as_view(), name="list_opros"),
    path("question_tekst/", views.Question_tekst.as_view(), name="question_tekst"),
    
    
]


