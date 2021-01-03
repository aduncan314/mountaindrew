"""Mountaindrew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('landing.app_urls', 'landing'), namespace='landing')),
    path('blog/', include('blog.blog_urls', namespace='blog'))
]
