from django.urls import path
from .views import *

urlpatterns = [
    path('', info_home_view, name='info_home'),
    path('<int:id>/', info_details_view, name='info_details'),
]
