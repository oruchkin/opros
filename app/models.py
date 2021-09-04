from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Opros(models.Model):
    creator = models.ForeignKey(User, related_name='user_id_like', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    opisanie = models.CharField(max_length=900)
    date_of_start = models.DateField(blank=True, null=True)
    date_of_end = models.DateField(blank=True, null=True)
    blocked = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.title}'


class Question_tekst(models.Model):
    opros_id = models.ForeignKey(Opros, on_delete=models.DO_NOTHING, related_name="question_for_opros")
    question_text = models.CharField(max_length=1000)
    question_answer = models.CharField(max_length=1000, blank=True, null=True) #здесь ошибка этого поля быть не должно, это ответ, в обьекте ответ
    # (не удалил чтобы остался доступ к "сайту")

    def __str__(self):
        return f'текущий вопрос {self.question_text}'
    

class Question_variant(models.Model):
    opros_id = models.ForeignKey(Opros, on_delete=models.DO_NOTHING, related_name="question_1variant")
    vopros = models.CharField(max_length=1000)
    variant_1 = models.CharField(max_length=1000, blank=True, null=True)
    variant_2 = models.CharField(max_length=1000, blank=True, null=True)
    variant_3 = models.CharField(max_length=1000, blank=True, null=True)
    variant_4 = models.CharField(max_length=1000, blank=True, null=True)
    mnogo = models.BooleanField(default=False)

    def __str__(self):
        return f'текущий вопрос {self.question_text}'
