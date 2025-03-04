from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views





urlpatterns = [
       path('', views.home, name='home'),
       path('post/new/', views.post_create, name='post_create'),
       path('post/<int:pk>/', views.post_detail, name='post_detail'),
       path('post/<int:pk>/edit/', views.post_update, name='post_update'),
       path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
       
       # Only signup, login/logout handled by Django auth
       path('signup/', views.signup, name='signup'),
   ]