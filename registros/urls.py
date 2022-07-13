from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',login_request,name='login'),
    path('registro',registro_request, name='registro'),
    path('logout',LogoutView.as_view(template_name='registros/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil' ),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)