from django.urls import path 
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'), 
    path('contato', views.contato, name='contato'),
    path('projetos', views.projetos, name='projetos'),
    path('equipe', views.equipe, name='equipe'),
    path('membros', views.membros, name='membros'),
    path('politica', views.politica, name='politica'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=getattr(settings, 'STATIC_ROOT', 'static'))
