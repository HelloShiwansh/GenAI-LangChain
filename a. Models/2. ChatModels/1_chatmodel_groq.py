from langchain_groq import ChatGroq

from dotenv import load_dotenv
# above line loads .env file and makes the environment variables available in the code

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=1.5, max_tokens=100)

#result = model.invoke("How many states in India?")
result = model.invoke("Give me 5 indian boys name")
print(result.content)