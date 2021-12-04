from django.urls import path
from .views import *

urlpatterns = [
    path('', wings_home_view, name='wings_home'),
    path('post/', paper_post_view, name='paper_post'),
    path('paper/<int:paper_id>/edit/', paper_edit_view, name='paper_edit'),
    path('paper/<int:paper_id>/', paper_details_view, name='paper_details'),
    path('paper/<int:paper_id>/delete/', paper_delete_view, name='paper_delete'),
]
