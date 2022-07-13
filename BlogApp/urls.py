from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio.as_view(), name='Inicio'),
    path('buscarCategoriaBlog/', buscarCategoriaBlog, name = 'buscarCategoriaBlog'),
    path('blog/nuevo/', blogCreacion.as_view(), name='blog_crear' ),
    path('blog/<pk>', postCreacion.as_view(), name='post_crear' ),
    path('nueva_categoria/', categoriaCreacion.as_view(), name='categoria_crear' ),
    path('blog/', blogLista.as_view(), name='blog_lista' ),
    path('blog/detalle/<pk>', blogDetalle.as_view(), name='blog_detalle' ),
    path('blog/edicion/<pk>', blogActualizar.as_view(), name='blog_editar' ),
    path('blog/borrar/<pk>', blogEliminar.as_view(), name='blog_borrar' ),
    path('categoria/<str:cats>/', CategoriaVista, name='categorias'),
    path('like/<pk>',LikeView, name='like_blog'),
    path('',include('registros.urls')),
    path('about/', about, name='about' ),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




