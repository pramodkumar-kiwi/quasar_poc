"""
Used for Chatbot lib
"""
import copy

import datetime
import json
import fredapi as fd
import spacy
from sec_api import FullTextSearchApi

from Quasar import settings
nlp = spacy.load("en_core_web_sm")

import openai
import tiktoken
from functools import reduce
from langchain.text_splitter import CharacterTextSplitter

from apps.common.constants import (
    NUM, OPEN_AI, OPEN_AI_MODEL, OPEN_AI_ROLE, MAX_LENGTH_TOKE,
    CHAT_AI_MODEL
)

chatbots = {}
conversations = {}
conversation = []


class Chatbot:
    """
    AI Chatbot implementation.

    This class represents a basic chatbot implementation. It provides functionality
     for interacting with users through text-based conversations.

    Usage:
    - Initialize an instance of the Chatbot class.
    - Use the `get_response` method to obtain a response from the chatbot based on user input.
    """
    def get_chatbot_response(self, message, session_id):
        """
        Get the chatbot response based on the given message.
        Args:
            message (str): The user's message or input.
            session_id (str): The user's session_id or input.
        Returns:
            str: The chatbot response to the user's message.
        """
        data = dict()
        data['role'] = OPEN_AI_ROLE['ai']
        data['current_datetime'] = str(datetime.datetime.now())
        error_msg = ("I apologize, but it seems that I don't have the information you're looking for at the moment."
                     "Please feel free to ask another question, and I'll do my best to assist you with that.")
        try:
            keywords = extract_keywords(message)
            if session_id == 'fred':
                extra_text = '<br><a href="https://fred.stlouisfed.org/" target="_blank">Refer by Fred</a>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="#">Click Graph</a>'
                short_keyword = reduce(lambda a, b: a + "+" + str(b), keywords)

                fred = fd.Fred(api_key=settings.FRED_KEY)
                fred_data = fred.search(short_keyword)
                if not fred_data.empty:
                    series_number = fred_data['id'][0]
                    result = fred.get_series(series_number)
                    str_value = result.to_string()
                    act_prompt = "This is" + str_value + "Data. Please give the summary of the above data in detailed points with headings and subheadings with percent value"
                    #act_prompt = str_value + "<br>this is  time series data of the question " + message + ". give answer to the question mentioned as a question in percent value"
                else:
                    str_value = None
            else:
                extra_text = '<br><a href="https://www.sec.gov/edgar" target="_blank">Refer by Edger</a>'
                short_keyword = reduce(lambda a, b: a + " " + str(b), keywords)
                full_text_search_data = FullTextSearchApi(api_key=settings.EDGER_KEY)
                query = {
                    "query": short_keyword,
                    "startDate": '2013-01-01',
                    "endDate": '2023-01-01',
                }
                filings = full_text_search_data.get_filings(query)
                if filings:
                    edger_dict = filings['filings'][0]
                    if filings['filings'][0] and filings['filings'][0]['filingUrl']:
                        extra_text = '<br><a href="https://www.sec.gov/edgar" target="_blank">Refer by Edger</a> &nbsp&nbsp&nbsp&nbsp&nbsp<a href="'+ filings['filings'][0]['filingUrl'] + '" target="_blank">Click Document</a>'
                    str_value = json.dumps(edger_dict)
                    act_prompt = "This is" + str_value + "Data. Please give the summary of the above data in detailed points with headings and subheadings"
                else:
                    str_value = None

            if str_value:
                prompt = act_prompt
                openai.api_key = settings.OPEN_GPT_KEY
                # Generate the summary
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=300,
                    temperature=0.7,
                    stop=None,
                    n=1
                )
                # Extract the summary from the response
                summary = response.choices[0].text.strip() + extra_text
            else:
                summary = error_msg
            data['message'] = summary
        except Exception as error:
            _ = error
            summary = error_msg
            data['message'] = summary
        # Create a graph
        return data

def extract_keywords(question):
    # Process the input question using spaCy
    doc = nlp(question)

    # Initialize a list to store keywords
    keywords = []

    # Iterate through the tokens in the processed text
    for token in doc:
        # Check if the token is a noun or an adjective or pronouns

        #print(token.text,"-----",token.pos_,"--",token.tag_)
        if token.pos_ in ("NOUN", "ADJ","PROPN"):
            keywords.append(token.text)

    return keywords

def get_ai_token_count(docs):
    """
        Calculates the total token count for a list of documents using the
         OpenAI GPT-3.5 model with Hugging Face tokenizers.

        Args:
            docs (list): A list of documents to count tokens from.

        Returns:
            int: The total count of tokens in the documents.
        """
    all_text = list()
    try:
        enc = tiktoken.encoding_for_model(OPEN_AI_MODEL)
        for index, doc_text in enumerate(docs):
            if index < NUM['five']:
                texts = doc_text.page_content
                num_tokens = len(enc.encode(texts))
                if num_tokens > MAX_LENGTH_TOKE[index]:
                    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
                        chunk_size=MAX_LENGTH_TOKE[index], chunk_overlap=NUM['hundred'], separator=". "
                    )
                    split_list = text_splitter.split_text(texts)
                    if len(split_list) > NUM['zero']:
                        copied_list = copy.deepcopy(docs[index])
                        copied_list.page_content = ''
                        copied_list.page_content = split_list[NUM['zero']]
                        all_text.append(copied_list)
                else:
                    copied_list = copy.deepcopy(docs[index])
                    all_text.append(copied_list)
    except Exception as error:
        _ = error
    return all_text


def get_chatgpt_response(prompt):
    """
        Generate a response using the ChatGPT model.
        Parameters:
            prompt (str): The prompt or input for generating the response.
        Returns:
            str: The generated response from the ChatGPT model.
    """
    response = openai.Completion.create(
        engine=CHAT_AI_MODEL,
        prompt=prompt,
        max_tokens=OPEN_AI['max_tokens']
    )
    return response.choices[NUM['zero']].text.strip()
