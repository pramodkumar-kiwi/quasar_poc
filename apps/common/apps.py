"""
common app.py file
"""
from django.apps import AppConfig


class CommonConfig(AppConfig):
    """
    This is registered home app with class CommonConfig
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.common'
