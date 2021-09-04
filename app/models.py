from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Opros(models.Model):
    creator = models.ForeignKey(User, related_name='user_id_like', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    opisanie = models.CharField(max_length=900)
    date_of_start = models.DateField(blank=True, null=True)
    date_of_end = models.DateField(blank=True, null=True)
    blocked = models.BooleanField(default=False) #можно удалить не используется

    def __str__(self):
        return f'{self.title}'


class Question_tekst(models.Model):
    opros_id = models.ForeignKey(Opros, on_delete=models.DO_NOTHING, related_name="question_for_opros")
    question_text = models.CharField(max_length=1000)
    question_answer = models.CharField(max_length=1000, blank=True, null=True) #здесь ошибка этого поля быть не должно, это ответ в обьекте ответ

    def __str__(self):
        return f'текущий вопрос {self.question_text}'


class Question_1variant(models.Model):
    opros_id = models.ForeignKey(Opros, on_delete=models.DO_NOTHING, related_name="question_1variant")

    question_text = models.CharField(max_length=1000)

    answer_1 = models.CharField(max_length=1000, blank=True, null=True)
    answer_2 = models.CharField(max_length=1000, blank=True, null=True)
    answer_3 = models.CharField(max_length=1000, blank=True, null=True)
    answer_4 = models.CharField(max_length=1000, blank=True, null=True)
    #add bool который будет чекать это еденичный вопрос или множественный, если множественный то одна лгика
    # если еденичный то другая

    def __str__(self):
        return f'текущий вопрос {self.question_text}'
