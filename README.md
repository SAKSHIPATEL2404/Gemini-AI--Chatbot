#  Gemini AI Chatbot

A conversational AI chatbot built with *Python* and *Google Gemini API, with an integrated **Weather Forecast Feature* 🌦.  
The chatbot can answer general queries and also provide *current weather + 3-day forecast* for any city entered by the user.

---

##  Features
- Chat with AI using Google Gemini API
- Get *current weather* and *3-day forecast* of any city
- Speech input/output support
- Simple Python project (easy to run locally)

---

## 🛠 Tech Stack
- Python 3
- Google Gemini API
- Requests (for API calls)
- dotenv (for API key management)

---

## 📂 Project Structure
GeminiAI_Chatbot/ │-- chatbot.py        # Main chatbot logic │-- gemini_api.py     # Gemini API integration │-- weather.py        # Weather forecast feature │-- data_fetcher.py   # Fetches weather data │-- speech_io.py      # Speech input/output │-- settings.py       # Configuration │-- requirements.txt  # Dependencies │-- README.md         # Project details
## ⚙ Setup & Run

1. Clone the repository:
   ```bash
   git clone https://github.com/SAKSHIPATEL2404/GeminiAI_Chatbot.git
   cd GeminiAI_Chatbot

2. Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux


3. Install dependencies:

pip install -r requirements.txt


4. Add your API key:
Create a .env file in the project root and add:

GEMINI_API_KEY=your_api_key_here
WEATHER_API_KEY=your_weather_api_key_here


5. Run the chatbot:

python chatbot.py


- Future Improvements

Add GUI using Tkinter/Streamlit

Store chat history

Voice-based interaction



👩‍💻 Author

Sakshi Patel
🌐 Web Developer | 🤖 Generative AI Enthusiast | 📊 Data Science Learner
📧 sakshi2003patel2003@gmail.com 
