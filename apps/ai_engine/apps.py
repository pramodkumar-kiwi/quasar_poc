"""
Config Apps
"""
from django.apps import AppConfig


class AiEngineConfig(AppConfig):
    """
    To create config apps
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ai_engine'
