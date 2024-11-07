from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Initialize the LLM model
llm = Ollama(model="llama3.2:1b")

# Define prompts
prompt_poem = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5-year-old child, with around 100 words.")
prompt_chat = ChatPromptTemplate.from_template("Let's have a cheerful conversation about {topic} with positive words.")

# Add routes to FastAPI app
add_routes(
    app,
    prompt_poem | llm,
    path="/poem"
)

add_routes(
    app,
    prompt_chat | llm,
    path="/chat"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8007)
