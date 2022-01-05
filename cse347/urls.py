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
    path('statistic/', include('statistic.urls')),
    path('wings/', include('wings_app.urls')),
    path('news/', include('info_app.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
