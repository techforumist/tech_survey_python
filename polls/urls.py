
from django.urls import path, include
from rest_framework import routers
from .views import QuestionView, OptionView


router = routers.DefaultRouter()
router.register('questions', QuestionView)
router.register('options', OptionView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]
