from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_name'),
    path('about/', about_page, name='about_name'),

    path('users/', include('users.urls', namespace='users')),



]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
