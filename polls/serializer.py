from rest_framework import serializers
from .models import Option, Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question','url')


