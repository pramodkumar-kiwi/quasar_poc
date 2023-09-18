"""
Constant file for Application Form related questions and prompts
"""
from datetime import date
today = date.today()
day, month, year = today.strftime("%d"), today.strftime("%m"), today.strftime("%Y")
QUESTIONS_1 = [
    "May I please have your first and/or middle name?",
    "Please enter your last name.",
    "Please enter your biological gender. (Male/Female)",
    "Where were you born? (Please mention state or country)",
    "Please enter your date of birth. (mm-dd-yyyy)",
]

PROMPTS_QUESTION_1 = [
    " the below string contains characters only then just answer correct else for numeric value or for any "
    "special characters then show use please write a proper  first name!!",
    "if the below string contains characters only then just answer correct else for numeric value or for "
    "any special characters then show use please give a proper name!!",
    "The below string should contain one gender only. If it does then answer correct else for any other value "
    "then show try again and ask the question again",
    "if the below string contains any country name or state name then just answer correct else for any other value "
    "then show try again",
    f"if the below string contains the  mm-dd-yyyy date format and is in the date range between 12-12-1800 "
    f"to {month}-{day}-{year} then just answer correct else for any value out of the given range show please try "
    f"again"
]

QUESTIONS_2 = [
    "Who is your employer?",
    "What is your occupation?",
    "What is the date of employment? (mm-dd-yyyy)"
]

PROMPTS_QUESTION_2 = [
    "Just print correct on any given string",
    "Just print correct on any given string",
    f"if the below string contains the  mm-dd-yyyy date format and is in the date range between 12-12-1800 "
    f"to {month}-{day}-{year} then just answer yes else for any value out of the given range answer no"
]

QUESTIONS_3 = [
    "What is the reason for your unemployment? (Retired / Student / Homemaker / Disabled / Other)"
]

PROMPTS_QUESTION_3 = [
    "If the given string contains Retired or Student or Homemaker or Disabled  or Others or retired or "
    "student or homemaker or other or Other or others then answer me yes else show no"
]

QUESTIONS_4 = [
    "Please provide the details of your beneficiary by entering their first and/or middle name.",
    "Please enter your beneficiary's last name.",
    "Please enter your beneficiary's date of birth. (mm-dd-yyyy)",
    "Please enter your beneficiary's Social Security Number? (Last 4 digits)",
    "Please enter your beneficiary's phone number. (XXX-XXX-XXXX)",
    "Please specify what type of relationship do you have with your beneficiary? (e.g. Friend/Father)",
    "Please enter your beneficiary's email address. (e.g. example@gmail.com)",
    "Please enter your beneficiary's current address. (Country, State, Block/Area, House/Flat)",
    "How much % of shares does your beneficiary owns? (e.g. 30%)"
]

PROMPTS_QUESTION_4 = [
    "if the below string contains characters only then just answer correct else for numeric value or for "
    "any special characters then show use please write a proper first name!!",
    "if the below string contains characters only then just answer correct else for numeric value or for "
    "any special character then show use please give a proper last name!!",
    f"if the below string contains the  mm-dd-yyyy date format and is in the date range between 12-12-1800 "
    f"to {month}-{day}-{year} then just answer correct else for any value out of the given range show "
    f"please try again",
    "Just print correct on any given string",
    "Just print correct on any given string",
    "Just print correct on any given string",
    "If the below string contains an @ and a dot then just answer correct else  show please write proper email address",
    "if the below text contains a valid address then just answer correct else for any other value "
    "show please try again",
    "if the below string contains any natural numbers/whole number/rational number  between 0 to 100 , "
    "then print it is correct else for any other value or negative numbers show please try again"
]

QUESTIONS_5 = [
    "When was the last date you used such a product? (mm-dd-yyyy)",
    "How often do you use nicotine containing products? (Often/not too often/I don't use them)",
]

PROMPTS_QUESTION_5 = [
    f"if the below string contains the  mm-dd-yyyy date format and is in the date range between 12-12-1800 "
    f"to {month}-{day}-{year} then just answer correct else for any value out of the given range show please "
    f"try again",
    "Just print correct on any given string"
]

QUESTIONS_6 = [
    "Please enter the date when you were diagnosed. (mm-dd-yyyy)",
    "What was the level of severity of your condition? (mild, moderate, severe, life-threatening)",
]

PROMPTS_QUESTION_6 = [
    f"if the below string contains the  mm-dd-yyyy date format and is in the date range between 12-12-1800 "
    f"to {month}-{day}-{year} then just answer correct else for any value out of the given range show please "
    f"try again",
    "Just print correct on any given string"
]

QUESTIONS_7 = ["What type of treatment did you receive?"]

PROMPTS_QUESTION_7 = [
    "Just print correct on any given string"
]

QUESTIONS_8 = [
    "What is the name of the medication which you are/were on?",
    "What dosage of this medicine were/are you taking?",
    "How frequently have you been/are taking it?",
    "How long have you been taking it? (XX years/Still taking it)"
]

PROMPTS_QUESTION_8 = [
    "Just print correct on any given string",
    "Just print correct on any given string",
    "Just print correct on any given string",
    "Just print correct on any given string"
]

QUESTIONS_9 = [
    "What date were you hospitalized?(mm-dd-yyyy)",
    "Where were you hospitalized? (country, town)",
    "Please enter your doctor's name?",
    "Please enter your doctor's email address: (e.g. example@gmail.com)",
    "Please enter the address of the hospital where you were "
    "hospitalised. (Country, State, Block/Area, Hospital Name)"
]

PROMPTS_QUESTION_9 = [
    f"if the below string contains the  mm-dd-yyyy date format and is in the date range between 12-12-1800 "
    f"to {month}-{day}-{year} then just answer correct else for any value out of the given range show "
    f"please try again",
    "if the below string contains any country/state/city name then just answer correct else "
    "for any other value then show try again",
    "if the below string contains characters only then just answer correct else for numeric value or for "
    "any special character then show use please write proper  first name!!",
    "If the below string contains an @ and a dot then just answer correct else  show please write proper email address",
    "if the below text contains a valid address then just answer correct else for any other value show please try again"
]

COMMON_QUESTIONS = [
    "May I ask for your current employment status? Are you currently employed? (Yes/No)",
    "Have you used TOBACCO or any other product containing NICOTINE in the last 5 years? (Yes/No)",
    "Have you ever had coronary artery disease, chest pain, angina, palpitations, high blood pressure, "
    "rheumatic fever, heart murmur, heart attack, fainting spells or other disorder of the heart? (Yes/No)",
    "Do you have diabetes or any disorder of the thyroid, pituitary, adrenals, pancreas or other "
    "endocrine disorder? (Yes/No)",
    "Did you have cancer, tumor, mass, or growth of any kind arising in or spreading to any organ or tissue of "
    "the body including the blood, bone marrow or lymph gland? (Yes/No)",
    "Mental or emotional disorder, depression, anxiety disorder, suicide attempt, post-traumatic stress disorder "
    "(PTSD), ADD (attention deficit disorder), ADHD (attention deficit / hyperactivity disorder), schizophrenia, "
    "bipolar disorder, or other psychosis, psychiatric or neurological disorder? (Yes/No)",
    "Within the past 12 months have you been under observation by a member of the medical profession or taking "
    "medication or treatment for any illness, condition or injury not mentioned? (e.g. Yes/No)",
    "Do you want to add another beneficiary? (Yes/No)",
    "Did you receive any treatment for it? (Yes/No)",
    "Were you prescribed with any type of medication? (Yes/No)",
    "Were you ever hospitalized? (Yes/No)",
    "Please enter your Social Security Number. (Last 4 digits)"
]

API_RESPONSE = {
    "invalid_input": "Please enter a valid response.",
    "thanks_msg": "Thanks for the information.",
    "good": "Okay, Good to Know that!!",
    "limit_exceed": "Share % cannot exceed 100 (You are left with {}%).",
    "invalid_answer": "Please enter your response in Yes or No.",
    "shares_left": "% of shares still left. ",
    "network_error": "Please try again."
}

TYPE1_QUESTIONS = [4, 21, 23]
TYPE2_QUESTIONS = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
TYPE3_QUESTIONS = [8, 10, 12, 14, 24]
TYPE5_QUESTIONS = [5, 7, 9, 11, 13, 15, 17, 25]
DATE_QUESTIONS = [7, 9, 11, 13, 15, 17, 25]
GENDER_LIST = ['male', 'female', 'other']
