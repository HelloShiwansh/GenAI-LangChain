from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_tokens=50
)

result = model.invoke("Give me 5 indian cricketers name")

print(result.content)