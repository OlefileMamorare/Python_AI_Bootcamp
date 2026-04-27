from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import os

load_dotenv(find_dotenv(), override=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")