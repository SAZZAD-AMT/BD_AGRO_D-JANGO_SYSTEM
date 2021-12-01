from django.contrib import admin
from django.urls import path, include
from bdagro import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('user.urls')),
    path('blog/',  include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('projects/', include('bdagro.urls')),

    #path('projects/', views.projects, name='projects'),
    #path('project/<str:pk>/', views.project, name='project'),
    #path('create-project/', views.createproject, name='create-project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
