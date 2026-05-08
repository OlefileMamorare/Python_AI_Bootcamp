from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import os

load_dotenv(find_dotenv(), override=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

response = chat.send_message("What is the capital of France?")
print(chat.history)