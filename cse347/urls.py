from django.contrib import admin
from django.urls import path, include
from bdagro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('user.urls')),
    path('blog/',  include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
