from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', Inicio.as_view(), name='Inicio'),
    path('busquedaCategoriaBlog/', busquedaCategoriaBlog, name = 'busquedaCategoriaBlog'),
    path('buscarCategoriaBlog/', buscarCategoriaBlog, name = 'buscarCategoriaBlog'),
    path('buscarBlog/', buscarBlog, name = 'buscarBlog'),
    path('blog/nuevo/', blogCreacion.as_view(), name='blog_crear' ),
    path('blog/', blogLista.as_view(), name='blog_lista' ),
    path('blog/detalle/<pk>', blogDetalle.as_view(), name='blog_detalle' ),
    path('blog/edicion/<pk>', blogActualizar.as_view(), name='blog_editar' ),
    path('blog/borrar/<pk>', blogEliminar.as_view(), name='blog_borrar' ),
    path('login/',login_request,name='login'),
    path('registro',registro_request, name='registro'),
    path('logout',LogoutView.as_view(template_name='BlogApp/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil' ),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
