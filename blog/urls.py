from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('createcontent/', views.create_post, name='create_post'),
    path('article/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/', views.cat_list, name='category'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)