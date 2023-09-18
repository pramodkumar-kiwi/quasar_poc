"""
Django Admin
"""
from django.contrib import admin
from django import forms
from .models import OpenAiConfig
from django.contrib.auth.models import Group, User

from ..common.constants import OPEN_AI
from ..common.messages.msg_validation import VALIDATION_MESSAGE


class OpenAiConfigAdminForm(forms.ModelForm):
    """
    AdminForm for handling OpenAiConfig model's validations
    """
    def clean_temperature(self):
        """
        This function is used to validate temperature of openai
        :return: temperature
        """
        temperature = self.cleaned_data.get('temperature')
        if temperature is not None and (
                temperature < OPEN_AI['min_temperature'] or temperature > OPEN_AI['max_temperature']):
            raise forms.ValidationError(VALIDATION_MESSAGE['temperature'])
        return temperature

    class Meta:
        """
        meta class for OpenAiAdminForm
        """
        model = OpenAiConfig
        fields = '__all__'


class OpenAiConfigAdmin(admin.ModelAdmin):
    """
    OpenAiAdmin for displaying OpenAi model in django admin
    """
    form = OpenAiConfigAdminForm
    list_display = ['temperature', ]

    def has_add_permission(self, request):
        """
        This function is used to disable the ability to add new entries
        :param request: request
        :return: False
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        This function is used to disable the ability to delete the single entry
        :param request: request
        :param obj: None
        :return: False
        """
        return False


admin.site.register(OpenAiConfig, OpenAiConfigAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
