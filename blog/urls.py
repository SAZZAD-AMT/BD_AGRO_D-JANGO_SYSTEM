from django.urls import path
from .views import blog_view

urlpatterns = [
    path('', blog_view, name="blog"),
]
