# To create common templates
import json as simplejson

from django import template
from django.utils.safestring import mark_safe

from Quasar.settings import BASE_URL, API_BASE_URL

register = template.Library()


@register.filter
def jsonify(o):
    """
    jsonify request
    :param o:
    :return: request data
    """
    return mark_safe(simplejson.dumps(o))


@register.simple_tag
def load_constant():
    """
    Register global variables
    :return: response
    """
    constants = {'base_url': BASE_URL, 'api_base_url': API_BASE_URL}
    response = mark_safe(simplejson.dumps(constants))
    return response
