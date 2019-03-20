from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, Option
from .serializer import QuestionSerializer

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
