# Import Python Libraries
import os
import openai
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from src.conn.llm import llm, embeddings

load_dotenv(dotenv_path="config/.env")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

neo4j_cv_vector_index = Neo4jVector.from_existing_graph(
        embedding = embeddings,
        url = NEO4J_URI,
        username = NEO4J_USERNAME,
        password = NEO4J_PASSWORD,
        index_name = 'calcViewName',
        node_label = 'CalculationView',
        text_node_properties = ['name','package','uri'],
        embedding_node_property = 'cv_embedding'
    )

def get_vector_graph_chain():
    '''Create a Neo4j Retrieval QA Chain. Returns top K most relevant calculation view'''
    vector_graph_chain = RetrievalQA.from_chain_type(
        llm, 
        chain_type="stuff", 
        retriever = neo4j_cv_vector_index.as_retriever(search_kwargs={'k':1}), 
        verbose=True,
        return_source_documents=True,
    )
    return vector_graph_chain