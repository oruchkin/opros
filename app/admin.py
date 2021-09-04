from django.contrib import admin
from . models import User,  Opros, Question_tekst, Question_variant, Answer

# Register your models here.

admin.site.register(User)
admin.site.register(Opros)
admin.site.register(Question_tekst)
admin.site.register(Question_variant)
admin.site.register(Answer)
