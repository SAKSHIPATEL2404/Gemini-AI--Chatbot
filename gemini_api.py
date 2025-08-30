# gemini_api.py
import openai
from settings import GEMINI_API_KEY

# Set API key
openai.api_key = GEMINI_API_KEY

# Conversation memory
conversation_history = []

def add_to_history(role, content):
    conversation_history.append({"role": role, "content": content})

def ask_gemini(conversation):
    response = openai.ChatCompletion.create(
        model="gemini-1",  # Replace with actual Gemini model
        messages=conversation
    )
    return response['choices'][0]['message']['content']

