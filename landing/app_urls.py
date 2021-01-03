"""Mountaindrew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

# from django.contrib import admin
from django.urls import path

from landing import views

urlpatterns = [
    path('', views.index, name='MountainDrew'),
    path('index', views.index, name='index'),
    path('cv', views.cv, name='cv')
]
