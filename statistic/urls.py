from django.urls import path
from .views import *

urlpatterns = [
    path('statistic/', statistic_view, name="statistic"),
     path('k18/', k18_view, name="k18"),
]
