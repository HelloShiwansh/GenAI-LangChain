from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Tool By Shiwansh")

model = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.2
)

user_input = st.text_input("Enter your prompt:")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)
