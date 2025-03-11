from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.polub_post, name='polub_post'),
    path('post/<int:pk>/komentarz/', views.dodaj_komentarz, name='dodaj_komentarz'),
    path('api/posts/', views.PostSblawatListAPIView.as_view(), name='api_post_list'),
]
