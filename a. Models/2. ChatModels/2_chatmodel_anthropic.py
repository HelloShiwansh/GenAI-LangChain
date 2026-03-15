from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

model = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0.2,
    max_tokens=50
)

result = model.invoke("Give me 5 Indian boys names")

print(result.content)