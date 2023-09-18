"""
 Define valid character limit & min & max validation
 Used for validation dic
 Used for message validation
 Used for temperature validation
"""

# To define char limit
CHAR_LIMIT_SIZE = {
    'max_message_length': 1000,
}

# Define Validation message for all request submission

VALIDATION = {
    'message': {
        "blank": "MESSAGE_REQUIRED",
        "min_length": "MESSAGE_MIN_LENGTH",
        "max_length": "MESSAGE_MAX_LENGTH",
        "required": "MESSAGE_REQUIRED"
    }
}

VALIDATION_MESSAGE = {
    'temperature': 'Temperature must be from 0 to 1.'
}
