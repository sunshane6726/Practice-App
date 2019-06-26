from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
   path('<int:blog_id>/', views.detail, name = 'detail'),
   path('new/', views.new, name = 'new'),
   path('create/', views.create, name = 'create'),
   path('newblog/',views.blogpost, name='nowblog'),
] 
