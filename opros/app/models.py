from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass

class Opros(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(User, related_name='user_id_like', on_delete=models.CASCADE)
 
    def __str__(self):
        return f'опроссник: {self.title}'
    
# class TypeOfQuestion(models.Model):
#     type_of_question = models.CharField(max_length=1000)
    
#     def __str__(self):
#         return f'Тип вопроса: {self.type_of_question}'
    
class Question_tekst(models.Model):    
    opros_id = models.ForeignKey(Opros, on_delete=models.CASCADE, related_name="question_for_opros")       
    question_text = models.CharField(max_length=1000)
    question_answer = models.CharField(max_length=1000)
    
    def __str__(self):        
        return f'текущий вопрос {self.question_text}'


class Question_1variant(models.Model):    
    opros_id = models.ForeignKey(Opros, on_delete=models.CASCADE, related_name="question_1variant")  
        
    question_text = models.CharField(max_length=1000)
    
    answer_1 = models.CharField(max_length=1000, blank=True, null=True)
    answer_2 = models.CharField(max_length=1000, blank=True, null=True)
    answer_3 = models.CharField(max_length=1000, blank=True, null=True)
    answer_4 = models.CharField(max_length=1000, blank=True, null=True)
    
    def __str__(self):        
        return f'текущий вопрос {self.question_text}'
    
    
    
class Question_mnogo_variant(models.Model):    
    opros_id = models.ForeignKey(Opros, on_delete=models.CASCADE, related_name="question_mnogo_variant")     
    
    question_text = models.CharField(max_length=1000)
    
    answer_1 = models.CharField(max_length=1000, blank=True, null=True)
    answer_2 = models.CharField(max_length=1000, blank=True, null=True)
    answer_3 = models.CharField(max_length=1000, blank=True, null=True)
    answer_4 = models.CharField(max_length=1000, blank=True, null=True)
    
    def __str__(self):        
        return f'текущий вопрос {self.question_text}'
