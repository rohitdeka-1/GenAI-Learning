from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()
response = client.responses.create(
	model="gpt-4o-mini",
	input="Hey There"
)

print(response.output_text)