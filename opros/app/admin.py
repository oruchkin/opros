from django.contrib import admin

from . models import User, Opros, Question_tekst, Question_1variant, Question_mnogo_variant

# Register your models here.

admin.site.register(User)
admin.site.register(Opros)
admin.site.register(Question_tekst)
admin.site.register(Question_1variant)
admin.site.register(Question_mnogo_variant)
