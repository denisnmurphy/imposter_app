from . import views
from django.urls import path, include

urlpatterns = [
    path('questionone', views.question_one_detail),
    path('questiontwo', views.question_two_detail),
    path('questionthree', views.question_three_detail)
]
