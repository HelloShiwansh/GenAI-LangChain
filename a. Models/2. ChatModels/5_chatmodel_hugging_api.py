from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=256
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the President of India?")
print(result.content)