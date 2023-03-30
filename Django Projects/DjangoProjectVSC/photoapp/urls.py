from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Get the Main page, index
    path('<int:photo_id>/', views.detail, name='detail'),
]
