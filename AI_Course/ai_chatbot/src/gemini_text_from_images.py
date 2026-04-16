from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
import os
from PIL import Image

load_dotenv(find_dotenv(), override=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

img = Image.open("img.jpg")

text_prompt = "What is in this image?"

response = model.generate_content([text_prompt, img])
print(response.text)