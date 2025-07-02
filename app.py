import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# ✅ Corrected Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("Langchain Demo with Gemma Model")
input_text = st.text_input("What question do you have in mind?")

# LLM setup (Ollama + Gemma)
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()

# Combine everything into a chain
chain = prompt | llm | output_parser

# Handle user input
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
