"""
Django-application configuration for QuasarWeb.
"""
from django.apps import AppConfig


class GondolawebConfig(AppConfig):
    """
    Django-application configuration for QuasarWeb.
    This AppConfig class represents the configuration for the QuasarWeb Django application.
     It specifies the application name and the default auto-generated field for model primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QuasarWeb'
