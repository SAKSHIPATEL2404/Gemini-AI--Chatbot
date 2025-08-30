# chatbot.py
from gemini_api import add_to_history, ask_gemini, conversation_history
from data_fetcher import get_weather, get_bitcoin_price
from speech_io import listen, speak

def process_input(user_input):
    if "weather in" in user_input:
        city = user_input.split("weather in")[-1].strip()
        response = get_weather(city)
    elif "bitcoin" in user_input:
        response = get_bitcoin_price()
    else:
        add_to_history("user", user_input)
        response = ask_gemini(conversation_history)
        add_to_history("assistant", response)
    
    speak(response)
    return response

def main():
    print("=== Gemini AI Chatbot ===")
    print("Say 'exit' or 'quit' to stop.\n")
    
    while True:
        user_input = listen()
        if user_input in ["exit", "quit"]:
            speak("Goodbye!")
            print("Assistant: Goodbye!")
            break
        
        response = process_input(user_input)
        print(f"Assistant: {response}\n")

if __name__ == "__main__":
    main()

