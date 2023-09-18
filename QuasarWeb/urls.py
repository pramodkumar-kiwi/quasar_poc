"""
Uses for util urls

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:

"""
from django.urls import path

from QuasarWeb import views

urlpatterns = [
    path('', views.insurance, name='fred'),
    path('fred', views.insurance, name='fred'),
    path('edger', views.insurance, name='edger'),
]
