"""
Used for home page
"""
from django.shortcuts import render


def home(request):
    """
    Display home page
    :param request:
    :return: redirect to home page
    """
    return render(request, 'home/home.html')


def insurance(request):
    """
    Display insurance chat page
    :param request:
    :return: redirect to home page
    """
    return render(
        request, 'chat/insurance.html')


def application(request):
    """
    Display application chat page
    :param request:
    :return: redirect to home page
    """
    return render(
        request, 'chat/application.html')
