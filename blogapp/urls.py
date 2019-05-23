from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('blog/<int:blog_id>', views.detail, name="detail"),  
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"), 
]