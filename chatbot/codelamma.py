from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()#it will load the environment variables from the .env file
#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [("system","You are a coder and you can give all the code in a sequence way ")
     ,("user","Question:{question}")
        
    ]
)
# #{
#   "prompts": [
#     "System: You are a coder and you can give all the code in a sequence way 
# \nHuman: Question:table of 100 with nested loop in python"
#   ]
# }
## streamlit framework
st.title('Langchain Demo With LLAMA Code Model to help coders')
input_text=st.text_input("Search the topic u want code of")


#chain
llm=Ollama(model="codellama:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
 st.write(chain.invoke({"question":input_text}))

