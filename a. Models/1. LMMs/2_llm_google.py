from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

response = llm.invoke("What is the national bird of India?")
# response = llm.invoke(
#     "Answer in plain text without markdown formatting: What is the national bird of India?"
# )

print(response)