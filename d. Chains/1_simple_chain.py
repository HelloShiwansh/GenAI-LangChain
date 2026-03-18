from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.2
)

prompt = PromptTemplate(
    template="Give {count} facts about {topic}",
    input_variables=["count", "topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"count": 6, "topic": "AI"})
print(result)


chain.get_graph().print_ascii()