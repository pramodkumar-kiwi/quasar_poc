"""
Constant file used for global purpose constant variable for whole project
API_TITLE - Title for the API documentation
API_VERSION - Version of the API
API_VERSION_URL - URL path for API version
API_DESCRIPTION - Description for the API documentation
"""

# Define swagger api constant
API_TITLE = "Quasar API Document"
API_VERSION = "v1"
API_VERSION_URL = "api/" + API_VERSION + "/"
API_DESCRIPTION = 'Quasar Api Documentation'


OPEN_AI = {
    'min_temperature': 0,
    'max_temperature': 1,
    'max_tokens': 1000,
    'form_max_tokens': 100,
    'token_max_length': 12000,
    'max_text': 3000,
    'max_doc_limit': 5
}
OPEN_AI_MODEL = 'gpt-3.5-turbo-16k'
CHAT_AI_MODEL = 'text-davinci-003'
OPEN_AI_ROLE = {
    'ai': 'assistant',
    'content': "You are a helpful assistant.",
    'user': "user"
}

NUM = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'twenty_one': 21,
    'twenty_two': 22,
    'twenty_three': 23,
    'twenty_four': 24,
    'twenty_five': 25,
    'twenty_seven': 27,
    'hundred': 100,
    'minus_one': -1,
    'minus_two': -2,
    'minus_three': -3
}

NAME_REGEX = r'^[A-Za-z\s]+$'
SSN_REGEX = r'^\d{4}$'
DIGIT_REGEX = r'^[\d\s-]+$'
DATE_REGEX = r"(\d{2})(\d{2})(\d{4})"
DATE_FORMAT_REGEX = r'^(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])-\d{4}$'
DATE_FORMAT = '%m-%d-%Y'
PHONE_REGEX = r'^(\(\+)?(\+)?[\d\s()-]+$'
EMAIL_REGEX = r'^[-\w.]+@((?!(\w+\.){3,})[A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$'

REPLACE_STRING = "can you explain what"

MAX_LENGTH_TOKE = [4000, 4000, 3000, 2500, 2000]
