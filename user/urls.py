from django.urls import path
from .views import *

urlpatterns = [ 
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
    path('profile-update/', profile_update_view, name="profile_update"),
]
