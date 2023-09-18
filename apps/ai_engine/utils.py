"""
This utility used for common purpose for AI related modules
"""
import re
from datetime import datetime, date

import openai

from apps.ai_engine.question_constants import (
    QUESTIONS_1, PROMPTS_QUESTION_1, QUESTIONS_2, PROMPTS_QUESTION_2, QUESTIONS_3, PROMPTS_QUESTION_3, QUESTIONS_4,
    PROMPTS_QUESTION_4, QUESTIONS_5, PROMPTS_QUESTION_5, QUESTIONS_6, PROMPTS_QUESTION_6, COMMON_QUESTIONS,
    API_RESPONSE, TYPE2_QUESTIONS, PROMPTS_QUESTION_7, QUESTIONS_7, PROMPTS_QUESTION_8, QUESTIONS_8, PROMPTS_QUESTION_9,
    QUESTIONS_9, TYPE3_QUESTIONS, GENDER_LIST, TYPE5_QUESTIONS
)
from apps.common.constants import (
    NUM, OPEN_AI_MODEL, OPEN_AI_ROLE, OPEN_AI, NAME_REGEX, DIGIT_REGEX, DATE_REGEX, DATE_FORMAT_REGEX, PHONE_REGEX,
    SSN_REGEX, DATE_FORMAT, EMAIL_REGEX
)


def questions_mapping_dict():
    """
    This function is used to get mapped data for a question
    :return: mapping_dict
    """
    mapping_dict = {
        NUM['one']: {
            'prompt': PROMPTS_QUESTION_1, 'questions': QUESTIONS_1,
            'question_type': 27, 'next': COMMON_QUESTIONS[NUM['eleven']]},
        NUM['three']: {
            'prompt': PROMPTS_QUESTION_2, 'questions': QUESTIONS_2,
            'question_type': NUM['five'], 'next': QUESTIONS_4[NUM['zero']]},
        NUM['four']: {
            'prompt': PROMPTS_QUESTION_3, 'questions': QUESTIONS_3,
            'question_type': NUM['five'], 'next': QUESTIONS_4[NUM['zero']],
            'current_question': COMMON_QUESTIONS[NUM['seven']]},
        NUM['five']: {
            'prompt': PROMPTS_QUESTION_4, 'questions': QUESTIONS_4,
            'question_type': NUM['six'], 'next': COMMON_QUESTIONS[NUM['one']]},
        NUM['six']: {
            'questions': COMMON_QUESTIONS[NUM['two']], 'current_question': COMMON_QUESTIONS[NUM['one']],
            'next': QUESTIONS_5},
        NUM['seven']: {
            'prompt': PROMPTS_QUESTION_5, 'questions': QUESTIONS_5,
            'question_type': NUM['eight'], 'next': COMMON_QUESTIONS[NUM['two']]},
        NUM['eight']: {
            'questions': COMMON_QUESTIONS[NUM['three']], 'current_question': COMMON_QUESTIONS[NUM['two']],
            'next': QUESTIONS_6},
        NUM['nine']: {
            'prompt': PROMPTS_QUESTION_6, 'questions': QUESTIONS_6,
            'question_type': NUM['twenty'], 'next': COMMON_QUESTIONS[NUM['eight']]},
        NUM['ten']: {
            'questions': COMMON_QUESTIONS[NUM['four']], 'current_question': COMMON_QUESTIONS[NUM['three']],
            'next': QUESTIONS_6},
        NUM['eleven']: {
            'prompt': PROMPTS_QUESTION_6, 'questions': QUESTIONS_6,
            'question_type': NUM['twenty'], 'next': COMMON_QUESTIONS[NUM['eight']]},
        NUM['twelve']: {
            'questions': COMMON_QUESTIONS[NUM['five']], 'current_question': COMMON_QUESTIONS[NUM['four']],
            'next': QUESTIONS_6},
        NUM['thirteen']: {
            'prompt': PROMPTS_QUESTION_6, 'questions': QUESTIONS_6,
            'question_type': NUM['twenty'], 'next': COMMON_QUESTIONS[NUM['eight']]},
        NUM['fourteen']: {
            'questions': COMMON_QUESTIONS[NUM['six']], 'current_question': COMMON_QUESTIONS[NUM['five']],
            'next': QUESTIONS_6},
        NUM['fifteen']: {
            'prompt': PROMPTS_QUESTION_6, 'questions': QUESTIONS_6,
            'question_type': NUM['twenty'], 'next': COMMON_QUESTIONS[NUM['eight']]},
        NUM['sixteen']: {
            'questions': API_RESPONSE['thanks_msg'], 'current_question': COMMON_QUESTIONS[NUM['six']],
            'next': QUESTIONS_6},
        NUM['seventeen']: {
            'prompt': PROMPTS_QUESTION_6, 'questions': QUESTIONS_6,
            'question_type': NUM['twenty'], 'next': COMMON_QUESTIONS[NUM['eight']]},
        NUM['eighteen']: {
            'questions': COMMON_QUESTIONS[NUM['one']], 'current_question': COMMON_QUESTIONS[NUM['seven']],
            'next': QUESTIONS_4},
        NUM['twenty_one']: {
            'prompt': PROMPTS_QUESTION_7, 'questions': QUESTIONS_7,
            'question_type': NUM['twenty_two'], 'next': COMMON_QUESTIONS[NUM['nine']]},
        NUM['twenty']: {
            'questions': COMMON_QUESTIONS[NUM['nine']], 'current_question': COMMON_QUESTIONS[NUM['eight']],
            'next': QUESTIONS_7},
        NUM['twenty_two']: {
            'questions': COMMON_QUESTIONS[NUM['ten']], 'current_question': COMMON_QUESTIONS[NUM['nine']],
            'next': QUESTIONS_8},
        NUM['twenty_three']: {
            'prompt': PROMPTS_QUESTION_8, 'questions': QUESTIONS_8,
            'question_type': NUM['twenty_four'], 'next': COMMON_QUESTIONS[NUM['ten']]},
        NUM['twenty_four']: {
            'questions': COMMON_QUESTIONS[NUM['three']], 'current_question': COMMON_QUESTIONS[NUM['ten']],
            'next': QUESTIONS_9},
        NUM['twenty_five']: {
            'prompt': PROMPTS_QUESTION_9, 'questions': QUESTIONS_9,
            'question_type': NUM['ten'], 'next': COMMON_QUESTIONS},
    }
    return mapping_dict


def get_openai_token(user_answer, index, prompt):
    """
    This function is used to get token from openai
    :return: token
    """
    token = API_RESPONSE['invalid_input']
    if user_answer:
        try:
            first_ques = prompt[index] + "\n\n" + user_answer
            response = openai.ChatCompletion.create(
                model=OPEN_AI_MODEL,
                messages=[
                    {"role": OPEN_AI_ROLE["ai"], "content": OPEN_AI_ROLE["content"]},
                    {"role": OPEN_AI_ROLE["user"], "content": first_ques}
                ],
                max_tokens=OPEN_AI['form_max_tokens']
            )

            token = response['choices'][NUM['zero']]['message']['content']
        except Exception as error:
            _ = error
            token = API_RESPONSE['network_error']
    return token


def get_type1_response_data(data, index, answer):
    """
    This function is used to get response for type1 questions
    :return: data
    """
    data['index'] = index
    data['question_type'] = NUM['two']
    data['question'] = API_RESPONSE['invalid_answer'] + " " + COMMON_QUESTIONS[NUM['zero']]
    if answer == 'yes':
        data['question_type'] = NUM['three']
        data['question'] = QUESTIONS_2[index]
    elif answer == 'no':
        data['index'] = index
        data['question_type'] = NUM['four']
        data['question'] = QUESTIONS_3[index]
    return data


def get_type2_response_data(
        token, data, question, index, questions, question_type, next_question, shared_amount,
        user_answer, medical_quest):
    """
    This function is used to get response for type2 questions
    :return: data
    """
    if (
            "correct" in token.lower() or "yes" in token.lower() or
            (re.match(NAME_REGEX, user_answer) and (
            question in [NUM['one'], NUM['five']] and index in [NUM['zero'], NUM['one']]) or
            question == NUM['twenty_five'] and index == NUM['two'])
    ):
        questions_length = len(questions) - NUM['one']
        data['index'] = index + NUM['one'] if questions_length > index else NUM['zero']
        data['question_type'] = question if questions_length > index else question_type
        data['question'] = questions[index+NUM['one']] if questions_length > index else next_question
        if question == NUM['twenty_five'] and index == NUM['four']:
            next_index_map = {NUM['ten']: NUM['four'], NUM['twelve']: NUM['five'], NUM['fourteen']: NUM['six']}
            data['medical_quest'] = medical_quest + NUM['two']
            data['question'] = API_RESPONSE['thanks_msg'] if (
                    medical_quest == NUM['sixteen']
            ) else next_question[next_index_map.get(medical_quest, NUM['three'])]
            data['question_type'] = None if medical_quest == NUM['sixteen'] else data['medical_quest']
        if (question == NUM['five'] and index == len(QUESTIONS_4)-1
                and int(user_answer) + shared_amount < NUM['hundred']):
            data['index'] = NUM['zero']
            data['question_type'] = NUM['eighteen']
            data['question'] = COMMON_QUESTIONS[NUM['seven']]
            data['shared_amount'] = int(user_answer) + shared_amount
        elif (question == NUM['five'] and index == len(QUESTIONS_4)-NUM['one']
              and int(user_answer) + shared_amount > NUM['hundred']):
            data['index'] = index
            data['question_type'] = question
            data['question'] = API_RESPONSE['limit_exceed'].format(NUM['hundred']-shared_amount) + " " + questions[index]
            data['shared_amount'] = shared_amount
    else:
        data['index'] = index
        data['question_type'] = question
        api_response = API_RESPONSE['invalid_input']
        try:
            if question == NUM['five'] and index == len(QUESTIONS_4)-NUM['one'] and int(user_answer) > NUM['hundred']:
                api_response = API_RESPONSE['limit_exceed'].format(NUM['hundred']-shared_amount)
        except Exception as e:
            _ = e
        data['question'] = api_response + " " + questions[index]
        if token == API_RESPONSE['network_error']:
            data['question'] = API_RESPONSE['network_error']
    return data


def get_type3_response_data(
        user_answer, data, index, questions, question_type, question, current_question, shared_amount, medical_quest):
    """
    This function is used to get response for type3 questions
    :return: data
    """
    data['index'] = index
    if user_answer == 'yes':
        data['question_type'] = question+NUM['one'] if (
                len(questions) - NUM['one'] > index or question in [NUM['twenty'], NUM['twenty_two']]
        ) else question+NUM['two']
        data['question'] = questions[index] if (
                question in TYPE2_QUESTIONS and question != NUM['eighteen']
        ) else questions
    elif user_answer == 'no':
        data['question'] = COMMON_QUESTIONS[NUM['one']] if question == NUM['four'] else question_type
        if question == NUM['four']:
            next_ques = NUM['six']
            if shared_amount < NUM['hundred']:
                next_ques = NUM['eighteen']
                data['question'] = str(NUM['hundred'] - shared_amount
                                       ) + API_RESPONSE['shares_left'] + COMMON_QUESTIONS[NUM['seven']]
        elif question == NUM['sixteen']:
            next_ques = None
        elif question in TYPE3_QUESTIONS:
            next_index_map = {NUM['ten']: NUM['four'], NUM['twelve']: NUM['five'], NUM['fourteen']: NUM['six']}
            next_ques = medical_quest + NUM['two']
            data['medical_quest'] = next_ques
            data['question'] = API_RESPONSE['thanks_msg'] if (
                    medical_quest == NUM['sixteen']
            ) else COMMON_QUESTIONS[next_index_map.get(medical_quest, NUM['three'])]
        else:
            next_ques = question + NUM['two']
        data['question_type'] = None if (
                question == NUM['twenty_four'] and medical_quest == NUM['sixteen']) else next_ques
    else:
        data['question_type'] = NUM['eighteen'] if (
                question == NUM['four'] and current_question is COMMON_QUESTIONS[NUM['seven']]
        ) else question
        data['question'] = API_RESPONSE['invalid_answer'] + " " + current_question
    return data


def get_type4_response_data(data, index, user_answer, question_type, next_question):
    """
    Get response of type4 questions
    :param data:
    :param index:
    :param user_answer:
    :return:
    """
    if (
            question_type == NUM['one'] and index == NUM['two'] and
            user_answer.lower() in GENDER_LIST
    ):
        data['index'] = index + NUM['one']
        data['question_type'] = question_type
        data['question'] = QUESTIONS_1[NUM['three']]
    elif (
            (len(user_answer) != NUM['one'] and user_answer[NUM['zero']] != "-") and (
            (question_type == NUM['twenty_seven'] and re.match(SSN_REGEX, user_answer)) or
            (question_type == NUM['five'] and index == NUM['three'] and re.match(SSN_REGEX, user_answer)) or
            (question_type == NUM['five'] and index == NUM['four'] and re.match(PHONE_REGEX, user_answer)))
    ):
        data['index'] = NUM['zero'] if question_type == NUM['twenty_seven'] else index+NUM['one']
        data['question_type'] = NUM['two'] if question_type == NUM['twenty_seven'] else question_type
        data['question'] = next_question[index] if (
                question_type == NUM['twenty_seven']) else next_question['questions'][index+NUM['one']]
    elif (
            ((question_type == NUM['five'] and index == NUM['six']) or
             (question_type == NUM['twenty_five'] and index == NUM['three'])) and
            re.match(EMAIL_REGEX, user_answer)
    ):
        data['index'] = index+NUM['one']
        data['question_type'] = question_type
        data['question'] = next_question['questions'][index+NUM['one']]
    else:
        data['index'] = index
        data['question_type'] = question_type
        current_question = next_question[NUM['eleven']] if (
                question_type == NUM['twenty_seven']) else next_question['questions'][index]
        data['question'] = API_RESPONSE['invalid_input'] + ' ' + current_question
    return data


def get_type5_response_data(user_answer, data, index, question_type, next_question):
    """
    This function is used to get response for type5 questions which includes date
    :return: data
    """
    user_answer = re.sub(r'[-/ ]', '', user_answer)
    if len(user_answer) == NUM['eight'] and re.match(DATE_REGEX, user_answer):
        if re.match(DIGIT_REGEX, user_answer):
            date_matches = re.match(DATE_REGEX, user_answer)
            if date_matches:
                month = date_matches.group(NUM['one'])
                day = date_matches.group(NUM['two'])
                year = date_matches.group(NUM['three'])
                user_answer = f"{month}-{day}-{year}"
                if not re.match(DATE_FORMAT_REGEX, user_answer):
                    set_response_data(data, index, question_type, next_question['questions'])
                else:
                    try:
                        dob_date = datetime.strptime(user_answer, DATE_FORMAT).date()
                        today = date.today()
                        if dob_date <= today:
                            next_index = NUM['zero']
                            next_question_type = NUM['twenty_seven']
                            next_new_question = COMMON_QUESTIONS[NUM['eleven']]
                            if question_type == NUM['three']:
                                next_index = NUM['zero']
                                next_question_type = NUM['five']
                                next_new_question = next_question['next']
                            elif question_type in TYPE5_QUESTIONS:
                                next_index = index+NUM['one']
                                next_question_type = question_type
                                next_new_question = next_question['questions'][index + NUM['one']]
                            data['index'] = next_index
                            data['question_type'] = next_question_type
                            data['question'] = next_new_question
                        else:
                            set_response_data(data, index, question_type, next_question['questions'])
                    except Exception as error:
                        set_response_data(data, index, question_type, next_question['questions'])
                        _ = error
    else:
        set_response_data(data, index, question_type, next_question['questions'])
    return data


def set_response_data(data, index, question_type, question):
    """
    set response data
    """
    data['index'] = index
    data['question_type'] = question_type
    data['question'] = API_RESPONSE['invalid_input'] + ' ' + question[index]
