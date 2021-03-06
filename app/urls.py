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
    
    # API #opros
    path("list_opros/", views.List_Opros_api.as_view(), name="list_opros"),
    path("detailed_opros/<int:pk>/", views.Detailed_Opros_api.as_view(), name="detailed_opros"),
    
    # vopros s tekstom    
    path("question_tekst/", views.Question_tekst_api.as_view(), name="question_tekst"),
    path("detailed_vopros/<int:pk>/", views.Question_tekst_detailed.as_view(), name="detailed_vopros"),
    
    # вопрос с вариантами (одиночными и множественными)
    path("question_variant/", views.Question_variant_list.as_view(), name="question_variant"),
    path("question_variant_detailed/<int:pk>/", views.Question_variant_list_detailed.as_view(), name="question_variant_detailed"),
        
    # ответы пользователей    
    path("answer_list/", views.Answer_list.as_view(), name="answer_list"),
    path("answer_detailed/<int:pk>/", views.Answer_detailed.as_view(), name="answer_detailed"),
    
]


