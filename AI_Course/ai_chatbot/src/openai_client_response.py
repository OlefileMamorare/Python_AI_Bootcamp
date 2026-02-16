from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import os

load_dotenv(find_dotenv(), override=True)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
response = client.responses.create(
    model = 'gpt-4o',
    input="You are a Sci-Fi writer and poet. Write a poem about a lonely robot exploring a futuristic city.",
    temperature=1
)

print(response.output_text)