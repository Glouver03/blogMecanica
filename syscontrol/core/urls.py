from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', views.index  , name= 'core' ),
    #path('aulas/', views.aulas, name='aulas'),
    #path('aulas/', views.post_list, name='post_list'),  # URL para a lista de postagens
    path('noticias/', views.noticias, name='noticias'),
    path('oficina/', views.oficina, name='oficina'),
    path('projetos/', views.projetos, name='projetos'),
    path('loja/', views.loja, name='loja'),
    path('contato/', views.contato, name='contato'),
    #path('post/<int:id>/', views.post_detail, name='post_detail'),
    #path('post_list/', views.aulas, name='aulas'),
    #path('post/new/', views.create_post, name='create_post'),
    path('post_list/', PostListView.as_view(), name='aulas'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)