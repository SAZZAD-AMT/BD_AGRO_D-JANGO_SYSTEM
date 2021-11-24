from django.urls import path
from .views import *

urlpatterns = [
    path('statistic/', statistic_view, name="statistic"),
]
