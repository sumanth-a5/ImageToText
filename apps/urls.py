from django.contrib import admin
from django.urls import path
from apps import views
urlpatterns = [
    path('', views.upload_image, name='func4'),
]