from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import os

load_dotenv(find_dotenv(), override=True)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
# response = model.generate_content("Explain the concept of Quantum Computing in simple terms.")

#Streaming response
prompt = "Explain the concept of Quantum Computing to a 10-year-old."
response = model.generate_content(prompt)

for chunk in response:
    print(chunk.text, end="")
    print("-" * 100)