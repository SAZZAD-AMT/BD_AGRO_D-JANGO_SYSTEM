from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_home_view, name='blog_home'),
    path('post/<int:blog_id>/', blog_details_view, name='blog_details'),
    path('post/new/', blog_post_view, name='blog_post'),
    path('post/<int:blog_id>/edit/', blog_edit_view, name='blog_edit'),
    path('post/<int:blog_id>/delete/', blog_delete_view, name='blog_delete'),
]
