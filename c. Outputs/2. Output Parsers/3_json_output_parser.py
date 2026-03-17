from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.2
)

parser = JsonOutputParser()

template = PromptTemplate(
    template= 'Give me the name, age, city of a fictional character \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)


# print(final_result)
# print(type(final_result))

chain = template | model | parser

result = chain.invoke({})

print(result)