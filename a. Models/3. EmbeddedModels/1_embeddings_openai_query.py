from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  
)

result = embeddings.embed_query("What is the capital of France?")
print(result[:5])  