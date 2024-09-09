from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# tag::llm[]
# Create the LLM
load_dotenv(dotenv_path="config/.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

llm = ChatOpenAI(
    openai_api_key= OPENAI_API_KEY,
    model= OPENAI_MODEL,
    temperature=0.0
)
# end::llm[]

# tag::embedding[]
# Create the Embedding model

embeddings = OpenAIEmbeddings(
    openai_api_key = OPENAI_API_KEY
)
# end::embedding[]
