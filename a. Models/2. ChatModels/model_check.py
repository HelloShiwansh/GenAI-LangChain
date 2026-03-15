from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

print("KEY:", os.getenv("GOOGLE_API_KEY"))   # debug

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

for m in client.models.list():
    print(m.name)