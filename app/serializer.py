from . models import Opros, Question_tekst, Question_variant, Answer
from rest_framework import serializers

class OprosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opros
        fields = "__all__"


class Question_tekst_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Question_tekst
        fields = "__all__"
        
        
class Question_variant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Question_variant
        fields = "__all__"


class Answer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
