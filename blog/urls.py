from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('users/<str:username>/', views.user_profile, name='user_profile'),
    path('tags/<slug:tag_slug>/', views.tagged_posts, name='tagged_posts'),
    path('signup/', views.signup_view, name='signup'),

]
