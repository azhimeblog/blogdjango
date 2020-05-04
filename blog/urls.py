from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('content/createcontent/', views.create_post, name='create_post'),
    path('article/<slug:slug>/', views.post_detail, name='post_detail'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)