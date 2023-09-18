"""
This view-set is responsible for handling API requests related to the AskBot model.
"""
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from apps.ai_engine.serializers.chatbot import AskBotSerializer, ApplicationFormSerializer
from apps.common.constants import NUM
from apps.common.utils import CustomResponse
from apps.common.viewsets import CustomModelViewSet


class AskBotViewSet(CustomModelViewSet):
    """
    View-set for handling chat data.

    This view-set is responsible for processing and handling API requests related to chat data.
     It utilizes the AskBotSerializer class for validating and serializing chat messages.

    The view-set allows only the 'post' HTTP method for creating new chat data.
    """
    serializer_class = AskBotSerializer
    http_method_names = ('post', )
    queryset = None

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        """
        Create a new chat message
        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response object.
        """
        session_id = self.request.GET.get('session_id', None)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'session_id': session_id})
        if serializer.is_valid():
            chat_data = serializer.save()
            csrf_token = get_token(request)
            chat_data['csrf_token'] = csrf_token
            return CustomResponse(status=status.HTTP_200_OK).success_response(chat_data)
        return CustomResponse(status.HTTP_400_BAD_REQUEST, serializer.errors).error_response()


class ApplicationFormViewSet(CustomModelViewSet):
    """
    View-set for handling Application form data.

    This view-set is responsible for processing and handling API requests related to application form.
     It utilizes the ApplicationFormSerializer class for validating and serializing questios and answers.

    The view-set allows only the 'post' HTTP method for creating new chat data.
    """
    serializer_class = ApplicationFormSerializer
    http_method_names = ('post', )
    queryset = None

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        """
        Create a new text
        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response object.
        """
        serializer_class = self.get_serializer_class()
        question_type = self.request.GET.get('question_type', NUM['zero'])
        index = self.request.GET.get('index', NUM['zero'])
        shared_amount = self.request.GET.get('shared_amount', NUM['zero'])
        medical_quest = self.request.GET.get('medical_quest', NUM['eight'])
        serializer = serializer_class(data=request.data, context={
            'question_type': question_type, 'index': index, 'shared_amount': shared_amount,
            'medical_quest': medical_quest
        })
        if serializer.is_valid():
            text_data = serializer.save()
            return CustomResponse(status=status.HTTP_200_OK).success_response(text_data)
        return CustomResponse(status.HTTP_400_BAD_REQUEST, serializer.errors).error_response()
