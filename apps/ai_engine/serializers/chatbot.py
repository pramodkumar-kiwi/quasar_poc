"""
This module contains the AskBotSerializer class, which is used for serializing
 and validating chat data.
"""
from rest_framework import serializers

from apps.ai_engine.chatbot import Chatbot
from apps.ai_engine.question_constants import (
    QUESTIONS_1, TYPE1_QUESTIONS, TYPE2_QUESTIONS, COMMON_QUESTIONS, DATE_QUESTIONS
)
from apps.ai_engine.utils import (
    questions_mapping_dict, get_type3_response_data, get_type2_response_data, get_type1_response_data,
    get_openai_token, get_type4_response_data, get_type5_response_data
)
from apps.common.constants import NUM, REPLACE_STRING
from apps.common.messages.msg_validation import VALIDATION, CHAR_LIMIT_SIZE

chat_bot = Chatbot()


class AskBotSerializer(serializers.Serializer):
    """
    The AskBotSerializer class is a serializer used for validating and serializing chat data.
    It is a CharField serializer field.
    """
    message = serializers.CharField(
        max_length=CHAR_LIMIT_SIZE['max_message_length'],
        required=True, allow_blank=False,
        error_messages=VALIDATION['message']
    )

    def save(self):
        """
        Create a chat instance.
        Args:
            self (dict): self request.
        """
        message = self.validated_data['message'].strip()
        message_lower = message.lower()
        return chat_bot.get_chatbot_response(message_lower, self.context['session_id'])


class ApplicationFormSerializer(serializers.Serializer):
    """
    The ApplicationFormSerializer class is a serializer used for validating application form data.
    It includes a single field named answer, which represents the answers given by user
    """
    answer = serializers.CharField(
        max_length=CHAR_LIMIT_SIZE['max_message_length'],
        allow_blank=False, allow_null=True,
        error_messages=VALIDATION['message']
    )

    def save(self):
        """
        Create a chat instance.
        Args:
            self (dict): self request.
        """
        question_type = int(self.context['question_type'])
        index = int(self.context['index'])
        shared_amount = int(self.context['shared_amount'])
        medical_quest = int(self.context['medical_quest'])
        data = dict()
        user_answer = self.validated_data['answer']
        if question_type == NUM['zero']:
            data['index'] = index
            data['question_type'] = NUM['one']
            data['question'] = QUESTIONS_1[index]
        mapping_dict = questions_mapping_dict()
        if question_type == NUM['two']:
            data = get_type1_response_data(data, index, user_answer.lower())
        elif (
                question_type == NUM['twenty_seven'] or
                (question_type == NUM['five'] and index in [NUM['three'], NUM['four'], NUM['six']]) or
                (question_type == NUM['one'] and index == NUM['two']) or
                (question_type == NUM['twenty_five'] and index == NUM['three'])
        ):
            next_question = COMMON_QUESTIONS if question_type == NUM['twenty_seven'] else mapping_dict[question_type]
            data = get_type4_response_data(data, index, user_answer, question_type, next_question)
        elif (
                question_type in TYPE1_QUESTIONS or
                (question_type == NUM['one'] and index != NUM['four']) or
                (question_type in [NUM['three'], NUM['five']] and index != NUM['two']) or
                (question_type in DATE_QUESTIONS and index != NUM['zero'])
        ):
            user_answer = user_answer.upper() if (
                    question_type == NUM['three'] and index == NUM['zero']) else user_answer
            user_answer = user_answer.split('%')[NUM['zero']] if (
                    question_type == NUM['five'] and "%" in user_answer) else user_answer
            token = get_openai_token(user_answer, index, mapping_dict[question_type]['prompt'])
            data = get_type2_response_data(
                token, data, question_type, index, mapping_dict[question_type]['questions'],
                mapping_dict[question_type]['question_type'], mapping_dict[question_type]['next'],
                shared_amount, user_answer, medical_quest
            )
        elif (
                (question_type == NUM['one'] and index == NUM['four']) or
                (question_type in [NUM['three'], NUM['five']] and index == NUM['two']) or
                (question_type in DATE_QUESTIONS and index == NUM['zero'])
        ):
            data = get_type5_response_data(
                user_answer, data, index, question_type, mapping_dict[question_type])
        elif question_type in TYPE2_QUESTIONS:
            question_type = NUM['four'] if question_type == NUM['eighteen'] else question_type
            data = get_type3_response_data(
                user_answer.lower(), data, index, mapping_dict[question_type]['next'],
                mapping_dict[question_type]['questions'], question_type,
                mapping_dict[question_type]['current_question'], shared_amount, medical_quest)
        return data
