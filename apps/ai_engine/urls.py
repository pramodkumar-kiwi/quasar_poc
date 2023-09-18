"""
Uses for util urls

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:

"""
from django.urls import path, include

from apps.ai_engine.views.ai_chat import AskBotViewSet, ApplicationFormViewSet
from apps.common.routers import OptionalSlashRouter

# Routes define
router = OptionalSlashRouter()

router.register(r'ask-bot', AskBotViewSet, basename='ask_bot')
router.register(r'application-form', ApplicationFormViewSet, basename='application_form')

urlpatterns = [
    path('', include(router.urls)),
]
