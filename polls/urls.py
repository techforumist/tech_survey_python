
from django.urls import path, include
from rest_framework import routers
from .views import QuestionView


router = routers.DefaultRouter()
router.register('questions', QuestionView)

urlpatterns = [
    path('', include(router.urls))
]
