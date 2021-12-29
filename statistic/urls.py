from django.urls import path
from .views import *

urlpatterns = [
    path("", statistic_view, name="statistic"),
    path("k18/", k18_view, name="k18"),
    path("up21/", up21_view, name="up21"),
]
